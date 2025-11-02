# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app

# Expose Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app/main.py"]
