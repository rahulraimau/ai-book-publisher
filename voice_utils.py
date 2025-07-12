from gtts import gTTS
import tempfile
import os

def speak(text):
    """Convert text to speech and return temporary mp3 path"""
    tts = gTTS(text)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_file.name)
    return temp_file.name
