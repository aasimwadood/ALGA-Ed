
# -----------------------------
# File: app/ui/app.py
# -----------------------------

import streamlit as st
from app.backend import run_learning_session

st.title("ALGA-Ed Adaptive Learning System")

user_id = st.text_input("Enter User ID")
topic = st.text_input("Learning Topic")
high_contrast = st.checkbox("Enable High Contrast Mode")
large_text = st.checkbox("Enable Large Text")

if st.button("Start Learning") and user_id and topic:
    profile_data = {"preferences": {"high_contrast": high_contrast, "large_text": large_text}}
    session = run_learning_session(user_id, topic, profile_data)

    st.markdown(session["text"], unsafe_allow_html=True)
    st.image(session["image"], caption="Generated Visual Aid")
    st.audio(session["audio"])
    st.subheader("Quiz")
    for q in session["quiz"]:
        st.markdown(f"**Q:** {q['question']}")
        st.markdown(f"*A:* {q['answer']}")

