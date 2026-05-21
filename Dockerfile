# Use a lightweight, official Python image optimized for production
FROM python:3.10-slim

# Install system dependencies
# ffmpeg is strictly required by Whisper to process audio files
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements file first to leverage Docker's caching mechanism
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire src directory into the container
COPY src/ ./src/

# Expose the port FastAPI runs on
EXPOSE 8000

# Run the Uvicorn server when the container starts
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]