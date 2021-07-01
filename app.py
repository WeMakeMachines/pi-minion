from services import Caching
from weather import weather

from flask import Flask

app = Flask(__name__)

app.register_blueprint(weather)
