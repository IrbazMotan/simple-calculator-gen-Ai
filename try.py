{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP3NtORw5pJpW1pHUAXcVDL",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/IrbazMotan/simple-calculator-gen-Ai/blob/main/try.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "from transformers import pipeline\n",
        "\n",
        "# Initialize the text-to-speech pipeline\n",
        "tts = pipeline(\"text-to-speech\", model=\"suno/bark\")\n",
        "\n",
        "text_input = st.text_input(\"Enter text to convert to speech:\")\n",
        "\n",
        "if text_input:\n",
        "    audio = tts(text_input)\n",
        "    audio.write(\"output.wav\")\n",
        "\n",
        "    # Display the audio file in Streamlit\n",
        "    st.audio(\"output.wav\")"
      ],
      "metadata": {
        "id": "brOJefECFz9k"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}