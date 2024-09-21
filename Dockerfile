FROM python:3.11-slim


# Install Python dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy application code
COPY . /app
WORKDIR /app
EXPOSE 8501

CMD ["streamlit", "run", "Chatbot.py"]
