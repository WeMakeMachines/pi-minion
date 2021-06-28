import werkzeug

from flask import abort, Blueprint
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

@weather.route("/daily/<int:days>")
def daily(days):
    maximumDayRange = 8
    minimumDayRange = 1
    if days > maximumDayRange or days < minimumDayRange:
        # TODO Better error handling
        abort(500)
    return openWeatherMap.daily(days)
