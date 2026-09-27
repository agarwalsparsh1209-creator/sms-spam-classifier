# 📩 SMS / Email Spam Classifier

An end-to-end Machine Learning web application that classifies incoming SMS or Email messages into **Spam** or **Not Spam (Ham)**. Built using Python, Scikit-Learn, NLTK, and deployed using Streamlit.

---

##  Features
- **Real-Time Classification:** Instant prediction of messages.
- **NLP Preprocessing:** Text cleaning using NLTK (Tokenization, Lowercasing, Stopwords removal, and Stemming).
- **Interactive UI:** Built with Streamlit for a fast and responsive web interface.

---

## Tech Stack
- **Language:** Python
- **Machine Learning & NLP:** Scikit-Learn, NLTK
- **Libraries:** Pandas, NumPy
- **Web App:** Streamlit

---

##  Project Structure
```text
├── app.py                      # Streamlit application source code
├── model .pkl                  # Trained Machine Learning model
├── vectorizer .pkl             # Fitted TF-IDF Vectorizer
├── requirements.txt            # Project dependencies
├── SMS_SPAM_DETECTION.ipynb    # Model training and experimentation notebook
└── README.md                   # Project documentation
