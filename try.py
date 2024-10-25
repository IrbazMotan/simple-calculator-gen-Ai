INCLUDE_COLAB_LINK = True  # Or False, depending on your needs

# ... other code

if INCLUDE_COLAB_LINK:
    print("Including Colab Link...")  # Code to include the Colab link (if needed)

from transformers import pipeline

tts = pipeline("text-to-speech", model="suno/bark")  # Or your chosen model
