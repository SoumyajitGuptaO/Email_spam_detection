import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
PS = PorterStemmer()
def text_transform(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y=[]
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
        y.append(PS.stem(i))
    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Email/SMS spam classifier")
input = st.text_area("Enter the message")
if st.button('Predict'):
    # Steps
    # 1.Preprocess
    transformed_input = text_transform(input)
    # 2.Vectorize
    vector_input = tfidf.transform([transformed_input])
    # 3.Predict
    result = model.predict(vector_input)[0]
    # 4.Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not spam")
