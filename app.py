import streamlit as st
import pickle
import numpy as np
import string
from nltk.corpus import stopwords
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Load models
tfidf = pickle.load(open('vectorizer .pkl', 'rb'))
model = pickle.load(open('model .pkl', 'rb'))

st.title("📩 SMS Spam Classifier")

input_sms = st.text_area("Enter your message")

# Button
if st.button("Predict"):

    transformed_sms = transform_text(input_sms)

    vector_input = tfidf.transform([transformed_sms]).toarray()

    num_characters = len(input_sms)

    vector_input = np.hstack((vector_input, [[num_characters]]))

    result = model.predict(vector_input)[0]

    if result == 1:
        st.error("🚨 Spam Message")
    else:
        st.success("✅ Not Spam")
