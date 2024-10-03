from flask import Flask, request, render_template
import pickle
import pandas as pd
import re
from nltk.corpus import stopwords
import nltk

app = Flask(__name__)

with open('model/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('model/vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = re.sub(r'\W', ' ', text)
    text = text.lower()
    text = [word for word in text.split() if word not in stop_words]
    return ' '.join(text)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    processed_text = preprocess_text(text)
    vectorized_text = vectorizer.transform([processed_text])
    prediction = model.predict(vectorized_text)
    result = "AI-generated" if prediction == 1 else "Human-generated"
    return render_template('index.html', prediction_text=result, input_text=text)

if __name__ == "__main__":
    app.run(debug=True)
