# 🎬 Movie Review Sentiment Classifier

This project is a web-based sentiment analysis tool that classifies movie reviews as **Positive** or **Negative** using a pre-trained deep learning model on the IMDb dataset. Built with TensorFlow and Streamlit, it provides an interactive interface for users to input reviews and receive instant sentiment predictions.

## 🚀 Features

- Classifies movie reviews into **Positive** or **Negative** sentiment
- Uses a pre-trained LSTM model trained on the IMDb dataset
- Real-time prediction with confidence score
- Clean and interactive UI built with Streamlit

## 🌐 Live Demo

The app is deployed and accessible on **Streamlit Cloud**:

👉 [Launch the App](https://movie-sentiment-classification-ht95vxbao2put8ghze89n3.streamlit.app/)


## 🧠 Model Details

- Dataset: IMDb Movie Reviews (from `tensorflow.keras.datasets`)
- Architecture: LSTM-based Sequential model (saved as `imdb.h5`)
- Input: Raw text reviews
- Output: Sentiment label and prediction score

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Animesh20112004/Movie-Sentiment-Classification.git
   cd movie-sentiment-classifier
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure the model file `imdb.h5` is in the project directory**

## 📦 Required Libraries

Make sure the following Python packages are installed:

- `numpy`
- `tensorflow`
- `streamlit`

You can install them using:

```bash
pip install numpy tensorflow streamlit
```

## ▶️ Running the App Locally

To launch the Streamlit app:

```bash
streamlit run main.py
```

Then open the provided local URL in your browser (usually `http://localhost:8501`).

## 🧾 Usage

1. Enter a movie review in the text area.
2. Click the **"Classify"** button.
3. View the predicted sentiment and the model's confidence score.

## 📁 Project Structure

```
movie-sentiment-classifier/
│
├── imdb.h5               # Pre-trained sentiment analysis model
├── main.py               # Streamlit app script
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies


## 📌 Notes

- The model uses a word index from the IMDb dataset to encode input text.
- Unknown words are handled with a fallback token.
- Input reviews are padded to a fixed length of 500 tokens.

