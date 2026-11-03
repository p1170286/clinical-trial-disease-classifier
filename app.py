from pathlib import Path

import joblib
import streamlit as st

MODEL_PATH = (
    Path(__file__).parent
    / "models"
    / "disease_classification.joblib"
)

model = joblib.load(MODEL_PATH)

st.set_page_config(
    page_title="Clinical Trial Disease Classifier",
    page_icon="🩺",
    layout="centered"
)

st.title("Clinical Trial Disease Category Classifier")
st.write(
    "Enter a clinical trial brief summary to predict its disease category."
)

summary = st.text_area(
    "Brief Summary",
    height=200,
    placeholder="Paste the clinical trial brief summary here..."
)

if st.button("Predict Disease Category"):
    if not summary.strip():
        st.warning("Please enter a brief summary.")
    else:
        prediction = model.predict([summary])[0]
        probabilities = model.predict_proba([summary])[0]
        confidence = max(probabilities)

        st.success(f"Predicted category: **{prediction}**")
        st.write(f"Model confidence: **{confidence:.1%}**")