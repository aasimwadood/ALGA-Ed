
import streamlit as st
from generate_aid import generate_aid
from evaluate_model import evaluate_model
from train_model import train
from preprocess import preprocess_data

st.set_page_config(page_title="ALGA-Ed AI Learning Aid", layout="centered")

st.title("🎓 ALGA-Ed: Adaptive Learning Aid for Students with Disabilities")

tab1, tab2, tab3 = st.tabs(["Generate Educational Aid", "Evaluate System", "Train Model"])

with tab1:
    st.header("🧠 Generate Customized Educational Aid")
    input_text = st.text_area("Enter topic or concept to simplify:")
    generate_button = st.button("Generate")

    if generate_button and input_text:
        output = generate_aid(input_text=input_text)
        st.success("Generated Content:")
        st.text_area("AI Output", value=output, height=300)

with tab2:
    st.header("📊 Evaluate System")
    test_data = st.text_area("Paste test data for evaluation:")
    if st.button("Evaluate"):
        metrics = evaluate_model(test_data)
        st.json(metrics)

with tab3:
    st.header("⚙️ Train AI Model")
    uploaded_file = st.file_uploader("Upload Dataset CSV", type=["csv"])
    if uploaded_file and st.button("Train Model"):
        data = preprocess_data(uploaded_file)
        result = train(data)
        st.success("Training Complete!")
        st.json(result)
