# Dockerfile

# Use the official lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Streamlit app code to the container
COPY streamlit_app.py .

# Expose Streamlit port
EXPOSE 8503

# Set environment variables
ENV OPENAI_API_KEY=""
ENV PINECONE_API_KEY=""
ENV PINECONE_ENVIRONMENT="us-east-1"
ENV INDEX_NAME="canopy--langchain"
ENV NAMESPACE="test-1"

# Command to run the Streamlit app
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8503", "--server.enableCORS=false"]
