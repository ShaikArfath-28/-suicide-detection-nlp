import streamlit as st
import re
import string
import joblib

# Load model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Clean function
def clean_text(text):
    text = re.sub(r"http\\S+", "", text)
    text = re.sub(r"@\\w+", "", text)
    text = re.sub(r"#\\w+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.strip().lower()

# UI
st.title("🧠 Mental Health Message Classifier")
st.markdown("Enter a message to detect if it's potentially suicide-related.")

input_text = st.text_area("Enter a tweet or message:")

if st.button("Predict"):
    if not input_text.strip():
        st.warning("Please type something.")
    else:
        cleaned = clean_text(input_text)
        vect = vectorizer.transform([cleaned])
        result = model.predict(vect)[0]

        if result == 1:
            st.error("⚠️ This might be a *Potential Suicide Post*")
        else:
            st.success("✅ This is *Not a Suicide Post*")
