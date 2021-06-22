from flask import Blueprint
from dotenv import dotenv_values
from services import OpenWeatherMap

config = dotenv_values(".env")

openWeatherMap = OpenWeatherMap(config['OPEN_WEATHER_MAP_API_KEY'], config['LATITUDE'], config['LONGITUDE']);

weather = Blueprint('weather', __name__, url_prefix='/weather')

@weather.route("/now")
def now():
    return openWeatherMap.now()

@weather.route("/hourly")
def hourly():
    return openWeatherMap.hourly()

@weather.route("/daily")
def daily():
    return openWeatherMap.daily()
