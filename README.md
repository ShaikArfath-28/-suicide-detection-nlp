# 🧠 Suicide Detection NLP App (Real-Time Twitter Message Classifier)

This is a **real-time machine learning app** that detects whether a message or tweet indicates potential suicide ideation. Built using **Python, scikit-learn, and Streamlit**, and trained on a Twitter-based mental health dataset.

## 🚀 Live App

🔗 [Click to Try the Live App](https://9yaem9m9shz8eg4wt8ljwx.streamlit.app/)

## 📂 Project Structure

├── app.py # Streamlit UI app
├── model.pkl # Trained logistic regression model
├── vectorizer.pkl # TF-IDF vectorizer
├── requirements.txt # Dependencies for Streamlit Cloud

## 📊 Model Info

- **Algorithm**: Logistic Regression  
- **Text Vectorization**: TF-IDF (Top 5000 features)  
- **Input**: Free text message (Tweet, SMS, etc.)  
- **Output**:
  - ✅ Not a Suicide Post
  - ⚠️ Potential Suicide Post

## 💻 Tech Stack

- Python 3.13
- Pandas, scikit-learn, joblib
- Streamlit for frontend
- Hosted on Streamlit Cloud

## 📦 How to Run Locally

```bash
git clone https://github.com/ShaikArfath-28/suicide-detection-nlp.git
cd suicide-detection-nlp
pip install -r requirements.txt
streamlit run app.py

## 🙋‍♂️ Author

**Shaik Arfath**  
Aspiring Data Analyst  
[LinkedIn](https://www.linkedin.com/in/shaik-arfath-a66318284/)

## 🧠 Disclaimer

This project is for educational/demo purposes only. It does not replace professional mental health advice.

