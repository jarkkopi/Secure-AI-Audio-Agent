import os
from src.utils.audio import transcribe_audio
from src.agent.graph import compiled_graph

audio_file = "src/tests/test.wav"

if os.path.exists(audio_file):
    # 1. Run your existing Whisper utility
    text = transcribe_audio(audio_file)
    
    # 2. Feed the text directly into your new LangGraph agent
    print("\n--- Starting Agent Processing ---")
    initial_state = {"transcript": text, "security_status": "pending", "output": ""}
    final_result = compiled_graph.invoke(initial_state)
    
    # 3. View the combined output
    print("\n--- Execution Finished ---")
    print("Final Output Payload:\n", final_result["output"])
else:
    print(f"Please place your '{audio_file}' file in the root directory.")