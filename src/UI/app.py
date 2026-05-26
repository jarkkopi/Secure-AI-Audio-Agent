import streamlit as st
import requests

# Set up page configurations
st.set_page_config(
    page_title="Secure Audio Agent",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ Secure AI Audio Agent")
st.markdown("Upload an audio file to transcribe, run cybersecurity filtering, and generate a concise summary.")

# 1. File Upload Section
uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3", "m4a", "flac"])

if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/wav")
    
    # Trigger execution on button click
    if st.button("Process Audio Pipeline", type="primary"):
        
        # 2. Status / Progress Section
        with st.spinner("Processing... Uploading audio, running local Whisper transcription, and executing LangGraph secure routing."):
            try:
                # Prepare payload for your FastAPI backend
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                
                # Make the request to your local running FastAPI server
                # (When running outside Docker, use localhost. If inside Docker, see below)
                response = requests.post("http://backend-api:8000/api/v1/process-audio", files=files)
                
                if response.status_code == 200:
                    data = response.json()
                    
                    st.success("Pipeline Execution Complete!")
                    st.divider()
                    
                    # 3. Result Section
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric(label="Filename", value=data.get("filename"))
                    with col2:
                        # Color code security status based on agent routing
                        status = data.get("security_status", "unknown").upper()
                        if status == "SAFE":
                            st.markdown(f"**Security Status:** 🟢 `{status}`")
                        else:
                            st.markdown(f"**Security Status:** 🔴 `{status}`")

                    st.subheader("Transcript Preview")
                    st.info(data.get("transcript_preview"))
                    
                    st.subheader("Final Output Summary")
                    st.write(data.get("result"))
                    
                else:
                    st.error(f"Backend Error ({response.status_code}): {response.json().get('detail', 'Unknown error')}")
                    
            except requests.exceptions.ConnectionError:
                st.error("Could not connect to the FastAPI backend server. Ensure `python -m src.main` is running on port 8000.")