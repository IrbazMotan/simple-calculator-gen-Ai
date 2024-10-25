import streamlit as st
from huggingface_hub import InferenceApi
import tempfile

# Initialize Hugging Face Inference API with the Bark model
# Replace 'YOUR_HUGGING_FACE_API_TOKEN' with your actual Hugging Face token
api = InferenceApi(repo_id="suno/bark", token="YOUR_HUGGING_FACE_API_TOKEN")

# Streamlit App for Text-to-Speech
st.title("Text-to-Speech App with Bark Model")

# Input Text
text_input = st.text_input("Enter text to convert to speech:")

# Function to Convert Text to Speech
def text_to_speech_bark(text):
    try:
        # Call the Bark model API for text-to-speech conversion
        response = api(text)
        
        # Save the audio to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            temp_audio.write(response["audio"].encode("ISO-8859-1"))
            temp_audio_path = temp_audio.name

        return temp_audio_path
    except Exception as e:
        return str(e)

# Generate and Play Audio
if text_input:
    audio_path = text_to_speech_bark(text_input)
    if isinstance(audio_path, str) and audio_path.endswith(".wav"):
        st.write("Audio Generated Successfully!")
        st.audio(audio_path)  # Play the audio in Streamlit
    else:
        st.write("Error generating audio:", audio_path)
