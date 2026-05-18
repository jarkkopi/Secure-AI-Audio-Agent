import whisper
# SPEECH TO TEXT TEST

print("Loading model...")
model = whisper.load_model("tiny")
print("Model loaded successfully!")

try:
    result = model.transcribe("test.wav")
    print("Transcript:", result["text"])
except Exception as e:
    print("Error:", e)