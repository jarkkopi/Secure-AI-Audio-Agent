# Secure AI Audio Agent Framework

A local-first AI orchestration pipeline designed to ingest multi-format audio streams, execute local transcription, filter real-time security vulnerabilities, and generate structured analytical summaries. 

By combining asynchronous backend routing with isolated microservices architecture, this framework ensures complete data privacy—processing sensitive auditory data strictly on-premise without reliance on external cloud APIs.

## System Architecture Overview
1. **Ingestion & UI:** A lightweight Streamlit interface captures audio uploads and streams payloads over a virtual bridge network.
2. **Transcription Engine:** An asynchronous FastAPI backend uses a local OpenAI Whisper utility to decode and transcribe auditory data.
3. **Security Orchestration:** A deterministic LangGraph state machine handles the transcript payload, routing it to a defensive security node.
4. **Vulnerability Mitigation:** A localized Small Language Model (SLM) inspects the transcript to detect and neutralize prompt injection or system override risks before passing clean data to the final summarization layer.

## Tech Stack
* **Orchestration:** LangGraph (Stateful, multi-agent routing workflows)
* **API Framework:** FastAPI (Asynchronous REST API endpoints & automated Swagger documentation)
* **Local Inference Engine:** Ollama running a hardware-optimized `qwen2.5:0.5b` model instance
* **Automatic Speech Recognition (ASR):** OpenAI Whisper (Natively executed)
* **Containerization & DevOps:** Docker & Docker Compose (Optimized multi-container microservices decoupling)
* **Web UI:** Streamlit (Responsive file-upload and status dashboard)

---

## Getting Started & Running Instructions

The entire environment is configured for a unified, single-command containerized deployment using Docker Compose. This ensures zero-configuration pathing and absolute environment isolation.

### Prerequisites
1. **Docker Desktop** installed, configured with WSL 2, and actively running in the system background.
2. **Ollama** installed natively on your host machine with the target SLM pre-cached:
   ```bash
   ollama pull qwen2.5:0.5b

### Execution
git clone

cd Secure-AI-Audio-Agent

docker compose build --no-cache

docker compose up
