from flask import Flask
from tensorflow.keras.applications import MobileNet

# Достаём модель
model = MobileNet(input_shape=(64, 64, 1), alpha=1., weights=None, classes=340)
model.load_weights('model.h5')

app = Flask(__name__)

from app import views