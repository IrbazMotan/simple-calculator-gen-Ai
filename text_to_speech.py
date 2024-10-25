import streamlit as st
import os
from huggingface_hub import InferenceApi
import tempfile

# Get the token from the environment variable
api_token = os.getenv("HUGGING_FACE_API_TOKEN")
if api_token is None:
    st.error("API token not found. Please set the HUGGING_FACE_API_TOKEN environment variable.")
else:
    # Initialize Hugging Face Inference API with the Bark model
    api = InferenceApi(repo_id="suno/bark", token=api_token)

    st.title("Text-to-Speech App with Bark Model")

    # Input for the text you want to convert
    text_input = st.text_input("Enter text to convert to speech:")

    def text_to_speech_bark(text):
        """Function to call Bark model and save audio response."""
        try:
            st.write(f"Input Text: {text}")
            
            response = api(text)  # Call API for text-to-speech
            st.write(f"API Response: {response}")  # Debugging output for response

            if "audio" not in response:
                return "Error: No audio in response."  # Handles missing audio key

            # Save audio to a temporary .wav file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
                temp_audio.write(response["audio"].encode("ISO-8859-1"))
                return temp_audio.name
        except Exception as e:
            st.error(f"Error: {str(e)}")
            return None

    # Generate audio if there's input
    if text_input:
        audio_path = text_to_speech_bark(text_input)
        if audio_path and audio_path.endswith(".wav"):
            st.audio(audio_path)
        else:
            st.write("Audio generation failed. Check logs for details.")
