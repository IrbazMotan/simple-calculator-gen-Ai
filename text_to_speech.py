import streamlit as st
from huggingface_hub import InferenceApi
import tempfile

# Initialize Hugging Face Inference API with Bark model
api_token =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  # Replace with your token
api = InferenceApi(repo_id="suno/bark", token=api_token)

st.title("Text-to-Speech App with Bark Model")

# Input for the text you want to convert
text_input = st.text_input("Enter text to convert to speech:")

def text_to_speech_bark(text):
    """Function to call Bark model and save audio response."""
    try:
        response = api(text)  # Call API for text-to-speech
        if "audio" not in response:
            return "Error: No audio in response."  # Handles missing audio key

        # Save audio to a temporary .wav file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            temp_audio.write(response["audio"].encode("ISO-8859-1"))
            return temp_audio.name
    except Exception as e:
        # Catch and display detailed error in Streamlit
        st.error(f"Error: {str(e)}")
        return None

# Generate audio if there's input
if text_input:
    audio_path = text_to_speech_bark(text_input)
    if audio_path and audio_path.endswith(".wav"):
        st.audio(audio_path)
    else:
        st.write("Audio generation failed. Check logs for details.")
