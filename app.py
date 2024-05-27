from flask import Flask, request, render_template, jsonify

import numpy as np
import tensorflow as tf
import os
from waitress import serve

# Load the saved model
loaded_model = tf.keras.models.load_model("mo.tf")
loaded_model.summary()

# Initalize the Flask app
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('text')
    sample = (text)
    prediction = loaded_model.predict(np.array([sample]))
    print(type(prediction[0]))
    print(prediction[0])
    response = {'prediction': float(prediction[0][0])}
    return jsonify(response)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 1000))
    serve(app, host='0.0.0.0', port=port)
