# Dockerfile
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code and data files
COPY app.py .
# Ensure your my_data folder is uploaded to the SAME level as app.py, Dockerfile etc.
COPY my_data /app/my_data


# Expose the port your Flask app will run on
EXPOSE 7860

# Set the command to run your Flask application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "--timeout", "120", "app:app"]