from flask import Flask, render_template, request, jsonify
import numpy as np
import librosa
import os

# Load your pre-trained model
model = 5

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    return

if __name__ == '__main__':
    app.run(debug=True)
