# Secure-AI-Audio-Agent
Building a production-ready API ingesting audio, checking for security issues and returning structured LLM summary. Framework containerized with Docker.

# Secure AI Audio Agent

A modular FastAPI and LangGraph pipeline that locally transcribes audio and uses a cybersecurity routing node to intercept prompt injection threats before summarizing the text.

## Tech Stack
- **Orchestration:** LangGraph
- **Local LLM / SLM:** Ollama lightweight option qwen2.5:0.5b
- **Transcription:** OpenAI Whisper (Local)
- **Environment:** Conda
- **UI:** streamlit


## Getting Started & Running Instructions

This project can be executed entirely containerized using Docker Compose

### Prerequisites
* **Docker Desktop** installed and actively running.
* **Ollama** installed on your host machine with the Qwen model pre-pulled:

  ollama pull qwen2.5:0.5b
- **Docker build:**
  
  docker compose build --no-cache
  
  docker compose up
  
