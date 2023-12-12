from flask import Flask
import tensorflow as tf


model = tf.keras.models.load_model('my_model.h5')

app = Flask(__name__)

from app import views