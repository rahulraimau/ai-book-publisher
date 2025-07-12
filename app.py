import streamlit as st
from pipeline import run_pipeline
from gtts import gTTS
import os

# Function to generate and return TTS audio file
def speak_text(text, filename="tts_output.mp3"):
    tts = gTTS(text)
    tts.save(filename)
    return filename

# UI starts here
st.set_page_config(page_title="AI Book Publisher", layout="wide")
st.title("📚 AI Book Publisher")

# Input field for Wikisource URL
chapter_url = st.text_input("Enter Wikisource Chapter URL", value="https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1")

# Run Pipeline
if st.button("Run Pipeline"):
    with st.spinner("🔁 Running pipeline..."):
        original, spun, reward = run_pipeline(chapter_url)

    # Show results
    st.subheader("📖 Original Text")
    st.text_area("Original", original, height=250)

    st.subheader("🧠 Spun Text")
    st.text_area("Spun", spun, height=250)

    st.subheader("🏆 RL Reward")
    st.json(reward)

    # Speak Spun Text
    if st.button("🔈 Speak Spun Text"):
        mp3_path = speak_text(spun[:300])  # Limit length for quick playback
        with open(mp3_path, "rb") as f:
            st.audio(f.read(), format="audio/mp3")
