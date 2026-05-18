import whisper
import os

# Loading whisper model, using tiny for fast inference.
_model = whisper.load_model("tiny")

def transcribe_audio(file_path: str) -> str:
    """
    Loads a local audio file, executes Whisper speech-to-text, 
    and returns the raw transcript string.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Audio file not found at: {file_path}")
        
    print(f"[Audio Utility] Transcribing file locally: {file_path}")
    
    # Run local inference
    result = _model.transcribe(file_path)
    
    transcript = result.get("text", "").strip()
    print(f"[Audio Utility] Transcription complete: '{transcript}'")
    
    return transcript