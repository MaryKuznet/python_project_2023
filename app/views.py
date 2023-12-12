from app import app, model
from flask import render_template, request, redirect, url_for
import sqlite3
import cv2
import base64
import numpy as np
import pickle
from PIL import Image
import io


with open('categories.pkl', 'rb') as file:
    categories = pickle.load(file)

# Домашняя страничка
@app.route('/')
def home():
    return render_template('base.html')

# Предсказание
@app.route('/predict', methods=['POST'])
def predict():
    draw = request.form['url'][22:]

    # Декодируем изображение
    draw_decoded = base64.b64decode(draw)
    bytes_io = io.BytesIO(draw_decoded)
    image = Image.open(bytes_io)
    image = np.array(image.convert('L'))

    # Изменение размера
    resized = cv2.resize(image, (64, 64), interpolation=cv2.INTER_AREA)
    vect = np.asarray(resized, dtype="uint8")
    vect[vect < 50] = 0
    vect[vect >= 50] = 255
    vect = vect.reshape(1, 64, 64, 1).astype('float32')

    # Получение предсказания
    my_prediction = model.predict(vect)
    index = np.argmax(my_prediction[0])
    final_pred = categories[index]

    return render_template('result.html', img_data=draw, prediction=final_pred)

# Хранилище
@app.route('/vault')
def vault():
    with sqlite3.connect('vault.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""
        SELECT name, predict, image
        FROM entries
        """)
        entries = cursor.fetchall()
        entries.reverse()
    return render_template('vault.html', entries=entries)

# Сохранение в хранилище
@app.route('/save', methods=['POST'])
def save():
    with sqlite3.connect('vault.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO entries (name, predict, image)
        VALUES (
            ?, ?, ?
        )
        """, (request.form['name'], request.form['predict'], request.form['image']))
    return redirect(url_for("home"))
