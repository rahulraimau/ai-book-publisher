import streamlit as st
from pipeline import run_pipeline
from voice_utils import speak_text

st.title("📚 AI Book Publisher")

chapter_url = st.text_input("Enter Wikisource Chapter URL", value="https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1")

if st.button("Run Pipeline"):
    original, spun, reward = run_pipeline(chapter_url)
    st.subheader("📖 Original Text")
    st.text_area("Original", original, height=250)

    st.subheader("🧠 Spun Text")
    st.text_area("Spun", spun, height=250)

    st.subheader("🏆 RL Reward")
    st.json(reward)

    if st.button("🔈 Speak Spun Text"):
        speak_text(spun)