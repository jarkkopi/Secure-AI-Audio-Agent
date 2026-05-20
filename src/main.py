import uvicorn
from fastapi import FastAPI
from src.api.router import router as api_router

# Initialize the FastAPI core framework
app = FastAPI(
    title="Secure AI Audio Agent API",
    description="A local, secure backend processing pipeline built with FastAPI and LangGraph.",
    version="1.0.0"
)

# Mount our modular API router
app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
def health_check():
    """ Simple health endpoint to verify the server is responsive. """
    return {"status": "healthy", "service": "secure-audio-agent"}

if __name__ == "__main__":
    # Run the development server locally on port 8000
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)