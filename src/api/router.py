import os
import shutil
from fastapi import APIRouter, UploadFile, File, HTTPException
from src.utils.audio import transcribe_audio
from src.agent.graph import compiled_graph

router = APIRouter()

@router.post("/process-audio/")
async def process_audio(file: UploadFile = File(...)):
    # validate file type
    if not file.filename.endswith((".wav", ".mp3", ".m4a")):
        raise HTTPException(status_code=400, detail="Unsupported file type. Please upload a valid audio file. (wav, mp3, m4a)")

    # save file to temp location
    temp_dir = "temp_uploads"
    os.makedirs(temp_dir, exist_ok=True)
    temp_file_path = os.path.join(temp_dir, file.filename)

    try:
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # transcribe audio using the utility function
        transcript = transcribe_audio(temp_file_path)

        # error if no transcript was generated
        if not transcript:
            raise HTTPException(status_code=500, detail="Failed to transcribe audio. No text generated.")

        # 4. Invoke the Graph Agent Layer (Phi-3 Engine)
        print("[API] Submitting transcript payload to LangGraph...")
        initial_state = {"transcript": transcript, "security_status": "pending", "output": ""}
        final_state = compiled_graph.invoke(initial_state)

        # 5. Return the finalized output payload
        return {
            "filename": file.filename,
            "transcript_preview": transcript[:100] + "..." if len(transcript) > 100 else transcript,
            "security_status": final_state["security_status"],
            "result": final_state["output"]
        }
    except Exception as e:
        print(f"[API Error] Exception caught during processing: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error during audio processing.")
        
    finally:
        # Clean up the temporary disk file immediately after execution to keep things secure
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
