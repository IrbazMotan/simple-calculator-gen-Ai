# try.py
INCLUDE_COLAB_LINK = True  # Or False, depending on your needs

# ... other code
if INCLUDE_COLAB_LINK:
    # Code to include the Colab link (if needed)
  # try.py
def my_function(include_colab_link=True):
  # ... other code
  if include_colab_link:
      # Code to include the Colab link (if needed)

# ... other code
my_function(include_colab_link=False)  # Pass False if not needed
from transformers import pipeline

tts = pipeline("text-to-speech", model="suno/bark")  # Or your chosen model
