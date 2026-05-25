# Secure-AI-Audio-Agent
Building a production-ready API ingesting audio, checking for security issues and returning structured LLM summary. Framework containerized with Docker.

# Secure AI Audio Agent

A modular FastAPI and LangGraph pipeline that locally transcribes audio and uses a cybersecurity routing node to intercept prompt injection threats before summarizing the text.

## Tech Stack
- **Orchestration:** LangGraph
- **Local LLM / SLM:** Ollama lightweight option qwen2.5:0.5b
- **Transcription:** OpenAI Whisper (Local)
- **Environment:** Conda
