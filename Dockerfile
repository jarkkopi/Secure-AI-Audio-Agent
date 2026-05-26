FROM python:3.10-slim

# Install system dependencies (ffmpeg is required by Whisper)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Exact version of PyTorch with CPU support
RUN pip install --no-cache-dir torch==2.12.0+cpu --extra-index-url https://download.pytorch.org/whl/cpu

# Install the remaining dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY src/ ./src/

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]