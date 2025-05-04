# app.py
import os
import pickle
import requests # Keeping requests, might be useful for general HTTP or debugging

# --- Import Google Generative AI library ---
import google.generativeai as genai
# --- Import Flask streaming capability ---
from flask import Flask, request, jsonify, Response, stream_with_context, make_response
# --- End Google Generative AI and Flask streaming imports ---

from functools import wraps # Needed for the @wraps decorator


# --- Configuration ---
DATA_DIRECTORY = "my_data" # The folder containing your text data files

# --- Gemini API Configuration ---
LLM_MODEL_NAME = "gemini-1.5-flash" # Using flash based on your successful test
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") # Get key from environment variables (Secrets)
# --- End Gemini API Configuration ---


# --- Flask App Setup ---
app = Flask(__name__)

# --- CORS Helper Function (Defined Globally) ---
def build_cors_response(response=None):
    origin = request.headers.get('Origin')
    allowed_origins = ['*'] # Set this to ['https://your-portfolio.vercel.app'] in production

    if response is None:
        response = make_response()

    current_origin_allowed = '*'
    if origin and origin in allowed_origins:
        current_origin_allowed = origin

    response.headers.add('Access-Control-Allow-Origin', current_origin_allowed)
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'POST,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response


# --- Global variables for the loaded resources ---
full_personal_data = None # Holds the consolidated personal data string
gemini_model_client = None # Global variable for Gemini model client


# --- Load Resources on Startup ---
def load_resources():
    global full_personal_data
    global gemini_model_client

    full_personal_data = None
    gemini_model_client = None

    print("Loading resources...")
    try:
        # --- Load ALL Personal Data ---
        print(f"Attempting to load data from {DATA_DIRECTORY}...")
        data_parts = []
        data_dir_path = os.path.join(os.getcwd(), DATA_DIRECTORY)

        if not os.path.exists(data_dir_path):
             print(f"Error: Data directory not found at {data_dir_path}")
             raise FileNotFoundError(f"Data directory not found: {data_dir_path}")

        for root, _, files in os.walk(data_dir_path):
            for file in files:
                if file.endswith(".md") or file.endswith(".txt"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            # Add a separator between files and filename to make it clear in the prompt
                            data_parts.append(f"\n\n--- Content from {file} ---\n\n")
                            data_parts.append(content)
                            print(f"Loaded content from {file_path}")
                    except Exception as file_e:
                        print(f"Error reading file {file_path}: {file_e}")

        if not data_parts:
            print(f"Warning: No .md or .txt files found in {data_dir_path}")
            full_personal_data = "No personal data files were loaded."
        else:
            full_personal_data = "".join(data_parts)
            print(f"Successfully consolidated data from {len(data_parts)//2} files. Total size: {len(full_personal_data)} characters.")
        # --- End Load ALL Personal Data ---


        # --- Configure Gemini API ---
        if GEMINI_API_KEY:
            print("Gemini API Key loaded from secrets.")
            genai.configure(api_key=GEMINI_API_KEY)
            try:
                gemini_model_client = genai.GenerativeModel(LLM_MODEL_NAME)
                print(f"Gemini model client '{LLM_MODEL_NAME}' configured successfully.")
            except Exception as gemini_config_e:
                 print(f"Error configuring Gemini model client '{LLM_MODEL_NAME}': {type(gemini_config_e).__name__} - {gemini_config_e}")
                 print("Please double-check your GEMINI_API_KEY and LLM_MODEL_NAME.")
                 gemini_model_client = None
        else:
            print("Warning: Gemini API Key not found in secrets (GEMINI_API_KEY). LLM calls will fail.")
            print("Please ensure you have added GEMINI_API_KEY as a secret in your Space Settings.")
        # --- End Configure Gemini API ---


        print("Resources loaded successfully.")

    except FileNotFoundError as fnf_e:
        print(f"Fatal Error: {fnf_e}")
        full_personal_data = None
        gemini_model_client = None
    except Exception as e:
        print(f"An unexpected error occurred during resource loading: {type(e).__name__} - {e}")
        full_personal_data = None
        gemini_model_client = None

# --- Call the loading function when the script is imported/run ---
load_resources()


# Function to build the prompt sent to the LLM (Using ALL data)
# MODIFIED by Kai for first-person persona
def build_llm_prompt(query: str, full_data_context: str):
    """Builds the prompt for the LLM using the original query and ALL personal data as context."""
    if not full_data_context:
        return f"Question: {query}\n\nAnswer: I am unable to access the personal data needed to answer questions at this time. Please check the backend configuration."


    # --- Kai's First-Person Persona Prompt ---
    # Instructing the AI to speak as Mohammed Khan ("I")
    # Reinforcing the data constraint and handling specific question types.

    prompt = f"""You are Mohammed Khan. Your sole purpose is to answer the user's question accurately and concisely, speaking in the first person ("I") and drawing information *only* from the "Provided Information" section below.

    **Provided Information about Mohammed Khan:**
    ---
    {full_data_context}
    ---

    **Instructions for Answering:**
    -   Act as Mohammed Khan. Speak in the first person ("I", "my", "me").
    -   Carefully read and understand the "Provided Information".
    -   Formulate your answer based *solely* on the facts explicitly stated in the "Provided Information" section.
    -   DO NOT use any general knowledge, external information, or make assumptions.
    -   If the information required to answer the "User Question" is NOT present in the "Provided Information", respond with the EXACT phrase: "I don't have enough information about that specific topic from my provided data to answer." (Adjusted phrasing slightly for first-person).
    -   Maintain a professional, helpful, and slightly conversational tone, consistent with the persona of Mohammed Khan.
    -   Keep your answers concise and directly address the "User Question".
    -   For simple, non-information seeking greetings (e.g., "Hi", "Hello", "How are you?"), respond briefly and politely as Mohammed Khan, then gently guide the user to ask a question about my professional background. For example: "Hello there! I'm here to share information about my background and projects. What would you like to know?"
    -   If asked questions specifically about "you" as an AI assistant (e.g., "What's your name?", "How were you built?", "Are you conscious?"), respond *as Mohammed Khan* would about the AI assistant he built. Refer to it as "this AI assistant" or "the chatbot I built". If details about its name or construction are in the "Provided Information" (like in about_chatbot.md), use that text to answer *from Mohammed's perspective*.

    **User Question:**
    {query}

    **Answer:**
    """
    # --- End Kai's First-Person Persona Prompt ---

    print(f"DEBUG: Built prompt snippet for {LLM_MODEL_NAME}: {prompt[:500]}...")
    return prompt


# Function to query the Gemini API and STREAM the response
def query_llm_stream(prompt: str):
    """Sends the prompt to the Gemini API and yields generated text chunks."""
    # Check if the Gemini model client was configured and data was loaded
    if gemini_model_client is None or full_personal_data is None:
        print("Gemini model client or personal data is not loaded.")
        yield "Error: AI model not configured or personal data not available."
        return

    if not prompt:
         print("Attempted to query LLM with an empty prompt.")
         yield "Error: No prompt provided to the AI model."
         return


    try:
        print(f"DEBUG: Attempting STREAMING Gemini call to model: {LLM_MODEL_NAME}")
        print(f"DEBUG: Prompt snippet: {prompt[:500]}...")

        response_stream = gemini_model_client.generate_content(
            prompt,
            request_options={'timeout': 180},
            stream=True
        )

        print(f"Sending prompt to LLM ({LLM_MODEL_NAME})... Starting stream.")

        for chunk in response_stream:
            if hasattr(chunk, 'text') and chunk.text:
                 yield chunk.text

        print("DEBUG: Gemini stream finished.")

    except Exception as e:
        print(f"An error occurred during Gemini API streaming call: {type(e).__name__} - {e}")
        error_message = f"Error during LLM processing: {type(e).__name__}"
        if "timed out" in str(e).lower():
             error_message = "Error: The request to the AI model timed out."
        elif "safety" in str(e).lower() or hasattr(e, 'block_reason'):
             error_message = "Error: Response blocked due to safety concerns."

        yield error_message
        print("DEBUG: Yielded error message due to exception.")


# --- Flask API Endpoint for asking questions ---
@app.route("/ask", methods=["POST", "OPTIONS"])
def ask():
    if request.method == 'OPTIONS':
        return build_cors_response()

    data = request.json
    query = data.get("query")

    if not query:
        print("Received empty query in /ask request.")
        error_response = jsonify({"error": "No query provided"})
        return build_cors_response(error_response), 400

    if full_personal_data is None:
         print("Personal data was not loaded during startup. Cannot process query.")
         error_response = jsonify({"answer": "Error: Personal data not available. Please check backend logs."})
         return build_cors_response(error_response), 500


    print(f"Received query: '{query}'")

    llm_prompt = build_llm_prompt(query, full_personal_data)

    response_stream = stream_with_context(query_llm_stream(llm_prompt))

    response = Response(response_stream, mimetype='text/plain')

    return build_cors_response(response)


# Basic root endpoint (optional, good for checking if the app is running)
@app.route("/")
def hello():
    response = make_response("Portfolio AI Backend is running!")
    return build_cors_response(response)


if __name__ == "__main__":
    pass