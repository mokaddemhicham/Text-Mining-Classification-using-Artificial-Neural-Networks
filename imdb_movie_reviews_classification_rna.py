# -*- coding: utf-8 -*-
"""IMDB Movie Reviews Classification RNA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FeRfEtGs6Q0Q62-QvLbqT1USr4oZNGoV

# Charger les données et Afficher les premières lignes
"""

import re
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
import tensorflow as tf

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

data = pd.read_csv("IMDB Dataset.csv")
print(data.head())

"""# Dictionnaire de données"""

data_dict = {
    "review": "Texte de la critique du film",
    "sentiment": "Sentiment associé à la critique (positif ou négatif)"
}
print(data_dict)

"""# Statistiques descriptives"""

print(data['sentiment'].value_counts() , "\n" )
print(data.describe() , "\n" )

"""# Visualisation des données"""

# Répartition des sentiments
plt.figure(figsize=(8,6))
sns.countplot(x='sentiment', data=data)
plt.title("Répartition des sentiments")
plt.show()

"""# Prétraitement des données"""

# Nettoyage des données
def clean_text(text):
    text = re.sub(r'<br />', ' ', text)
    text = re.sub('https://.*','', text)   #remove URLs
    text = re.sub(r'[^a-zA-Z ]', '', text)
    text = text.lower()
    return text

data['review'] = data['review'].apply(clean_text)
print(data.head())

"""# Encoder les sentiments"""

le = LabelEncoder()
data['sentiment'] = le.fit_transform(data['sentiment'])

"""# Séparer les données en ensembles d'entraînement et de test"""

X_train, X_test, y_train, y_test = train_test_split(data['review'], data['sentiment'], test_size=0.2, random_state=42)

"""# Tokenizer et padding"""

tokenizer = Tokenizer()
tokenizer.fit_on_texts(X_train)

vocab_size = len(tokenizer.word_index) + 1  # +1 pour le token de padding
X_train_seq = tokenizer.texts_to_sequences(X_train)
X_test_seq = tokenizer.texts_to_sequences(X_test)
X_train_pad = pad_sequences(X_train_seq, maxlen=100)
X_test_pad = pad_sequences(X_test_seq, maxlen=100)

"""# Construire et compiler le modèle"""

model = Sequential()
model.add(Embedding(input_dim=vocab_size, output_dim=64, input_length=100))
model.add(LSTM(64, return_sequences=True))
model.add(Dropout(0.5))
model.add(LSTM(64))
model.add(Dense(1, activation='sigmoid'))
model.summary()

"""# Compiler et Entraîner le modèle"""

# Compiler le modèle
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
# # Entraîner le modèle
history = model.fit(X_train_pad, y_train, epochs=5, batch_size=64, validation_data=(X_test_pad, y_test))

"""# Évaluer le modèle"""

# Évaluer le modèle
loss, accuracy = model.evaluate(X_test_pad, y_test)
print(f'Accuracy: {accuracy*100:.2f}%')

"""# Visualiser les résultats d'entraînement"""

# Tracer la perte d'entraînement et de validation
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Training and Validation Loss')
plt.legend()

# Tracer la précision d'entraînement et de validation
plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.title('Training and Validation Accuracy')
plt.legend()

plt.show()

"""# Making predictions"""

sample_text = (
    '''The movie by ENSA Berrechid was so good and the animation are so dope.
    I would recommend my friends to watch it.'''
)

# Nettoyer le texte d'échantillon
sample_text_cleaned = clean_text(sample_text)

# Convertir le texte en séquence de nombres entiers
sample_text_seq = tokenizer.texts_to_sequences([sample_text_cleaned])

# Appliquer du padding à la séquence
sample_text_pad = pad_sequences(sample_text_seq, maxlen=100)

# Prédire la classe du texte
predictions = model.predict(sample_text_pad)

# Afficher la probabilité prédite
print(predictions[0][0])

# Afficher l'étiquette basée sur la prédiction
if predictions[0][0] > 0.5:
    print('The review is positive')
else:
    print('The review is negative')

"""# Sauvegarder le modèle"""

model.save('imdb.keras')