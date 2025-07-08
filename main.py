import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.datasets import imdb
import streamlit as st

word_index=imdb.get_word_index()
reverse_word_index={value: key for key,value in word_index.items()}

model=load_model('imdb.h5')

# Step 2: Helper Functions
# Function to decode reviews
def decode_review(encoded_review):
    return ' '.join([reverse_word_index.get(i - 3, '?') for i in encoded_review])

# Function to preprocess user input
def preprocess_text(text):
    words = text.lower().split()
    encoded_review = [word_index.get(word, 2) + 3 for word in words]
    padded_review = sequence.pad_sequences([encoded_review], maxlen=500)
    return padded_review

def predict_sentiments(review):
    preprocessed_review=preprocess_text(review)
    prediction=model.predict(preprocessed_review)
    sentiment= 'Positive' if prediction[0][0] > 0.5 else 'Negative'
    return sentiment, prediction[0][0] 


st.title("This is a Moview Review system")
st.write("Enter the Movie Review to classify it as Positive or Negative.")

user_input=st.text_area('Movie Review')

if st.button('Classify'):
    sentiment, score=predict_sentiments(user_input)
    
    st.write(f"Sentiment : {sentiment}")
    st.write(f"Sentiment / Prediction Score : {score}")
else:
    st.write("Please Write a movie Review.")