# Secure-AI-Audio-Agent
Building a production-ready API ingesting audio, checking for security issues and returning structured LLM summary, within container.

# Secure AI Audio Agent

A modular FastAPI and LangGraph pipeline that locally transcribes audio and uses a cybersecurity routing node to intercept prompt injection threats before summarizing the text.

## Tech Stack
- **Orchestration:** LangGraph
- **Local LLM:** Ollama (Phi-3 Mini) / Lightweight option qwen2.5:0.5b
- **Transcription:** OpenAI Whisper (Local)
- **Environment:** Conda
