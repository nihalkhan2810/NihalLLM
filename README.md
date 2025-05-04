# 🤖 AI Portfolio Assistant

An interactive Chat LLM integrated on my portfolio, to answer questions about my Professional Background, Skills, and projects using a Custom AI Backend

---

## 🌐 Live Demo

Experience the AI Assistant live on my portfolio website:
[https://nihalportfolio-rho.vercel.app/] 

---

## ✨ Overview

This project is an AI-powered conversational agent embedded directly into my personal portfolio. It serves as an engaging alternative to traditional resume browsing, allowing recruiters and visitors to ask questions about my experience, education, projects, and skills in a natural language interface. 

## 🚀 Features

*   Answers questions about my professional background, projects, skills, and education.
*   Responds conversationally based on provided personal data.
*   Utilizes a Prompt Stuffing architecture for efficient data handling.
*   Integrates with the Google Gemini API for natural language understanding and generation.
*   Features a sleek, animated chat interface built with React.
*   Provides suggested questions to guide user interaction.
*   Ensures privacy by answering *only* based on provided information.

---


## 🧠 Architecture 



I tried to explore building a RAG pipeline for this project initially. I dove into **Google Colab** to process my data, used **Sentence Transformers** to create numerical representations of my text, built a searchable index with **FAISS**, and set up the logic in my backend.

While I wish that worked, it just didn't :( I realized that for a personal portfolio where all my data, though detailed, could fit comfortably within the context window of any of the modern LLM's – maintaining a separate RAG indexing system was actually adding more complexity than I needed *for this specific project*. Every time I updated my resume or added a new project, I'd have to go back to Colab, re-run the indexing pipeline, download files, and upload them to my backend. That felt like a lot of work.

So, I decided to make a  technical pivot. I decided to use the **Prompt Stuffing** architecture instead. This is much simpler for smaller datasets.

Here’s how the Prompt Stuffing works in my implementation:

1.  I consolidated all my personal data (everything from my projects, skills, education, etc.) into one big block of text when my backend application starts up.
2.  When you type a question into the chat, my backend takes your entire question and puts it together with that *entire consolidated text block* into a single, crafted prompt.
3.  This prompt also includes very strict instructions for the LLM (Google Gemini)
   
The **Prompt Stuffing** approach worked perfectly for my data size! It makes updating my information easy (I just edit the text files)

## 🛠️ My Tech Stack


### Frontend (My Portfolio Website & Chat Interface)

*   **React:** I built the entire user interface for t=my portfolio  from scratch using React.
*   **Tailwind CSS:** I used Tailwind to style everything
*   **Framer Motion:** To add the smooth animations to the UI
*   **React Icons:** I used this for the icons you see (like the chat bubble and arrow).
*   **Vercel:** for hosting and continuous deployment from GitHub.

### Backend (My AI API)

*   **Python:** I wrote the backend logic in Python.
*   **Flask:** to create the API endpoint that the chatbot talks to.
*   **Docker:** This makes sure it runs the same way no matter where it's deployed.
*   **Hugging Face Spaces:** I deployed my Docker container here. 
*   **Requests:** So that my backend can communicate with other web services, like for Google Gemini
### AI / ML Core

*   **Google Gemini API (gemini-2.0-flash):** I recommend this one, it's relatively cheaper and performs well enough. 
*   **Prompt Stuffing:** This is the specific architecture I chose to give the Gemini model access to all my personal data.
*   **(Initial Exploration) Sentence Transformers & FAISS:** Although I pivoted, I did explore using Sentence Transformers for embeddings and FAISS for vector search during my initial RAG research. Although it worked, it just didn't perform well. But it was a valuable experience. 

### Data Handling

*   **Plain Text Files (.md, .txt):**stored all my personal data in simple, structured text files.
*   **Python File I/O:** My backend code reads these files directly to build the data context.

---

## 🤔 Concluding Thoughts & Future Potential

My approach here, utilizing **Prompt Stuffing** with the Google Gemini API on free tiers, was a  choice driven by the project's specific scope and the desire for easy data updates with limited computational resources(I don't have a GPU)

Again, it's important to note that there are definitely other, more sophisticated approaches for handling custom data with LLMs, particularly **Retrieval Augmented Generation (RAG)** and *is* generally the superior architecture for:
*   **Massive Datasets:** When the volume of data exceeds the LLM's context window limits (hundreds or thousands of pages).
*   **Highly Dynamic Data:** Although Prompt Stuffing is okay for updates, complex RAG pipelines can be built to handle very frequent or large-scale data changes more efficiently.
*   **Optimized Retrieval:** allows for fine-tuning the retrieval process itself 

If I had access to better computational resources  and were dealing with a much larger, constantly growing dataset, I would most likely go with **RAG implementation**. 



---

## 📧 Contact

Feel free to reach out to me! You can find my contact information on my portfolio website or connect with me on [LinkedIn](https://linkedin.com/in/nihal-khan-49522818b/).

