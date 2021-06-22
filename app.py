import logging
import sys

from weather import weather

from flask import Flask

logging.basicConfig(filename="pi_minion.log",level=logging.ERROR)

app = Flask(__name__)

app.register_blueprint(weather)
