from flask import Flask,request, url_for, redirect, render_template, jsonify
import sys
import pandas as pd
import pickle
import numpy as np
import tensorflow as tf

print(tf.__version__)
print(sys.version)

# Load the saved model
loaded_model = tf.keras.models.load_model("mo.tf")

loaded_model.summary()
sample_text = (
	'''The movie by ENSA berrechid was so good and the animation are so dope.
	I would recommend my friends to watch it.'''
)
predictions = loaded_model.predict(np.array([sample_text]))
print(type(predictions))
print(*predictions[0])

if predictions[0] > 0:
	print('The review is positive')
else:
	print('The review is negative')
 

# Initalize the Flask app
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
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
    app.run(host='0.0.0.0', port=1000,debug=True)
