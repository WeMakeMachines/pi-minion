import logging

from flask import abort, Blueprint, request
from dotenv import dotenv_values
from services import Caching, OpenWeatherMap
from middleware import caching

config = dotenv_values(".env")

logging.basicConfig(filename="pinion.weather.info.log",level=logging.INFO, format="%(asctime)s:%(message)s")

open_weather_map = OpenWeatherMap(config['OPEN_WEATHER_MAP_API_KEY'], config['LATITUDE'], config['LONGITUDE']);

weather = Blueprint('weather', __name__, url_prefix='/weather')

@weather.route("/now")
def now():
    return open_weather_map.now()

@weather.route("/hourly")
@caching(60)
def hourly():
    
    if request.cacheable == True:
        data = open_weather_map.hourly()
        request.cache.write(data)

    else:
        data = request.cache.read()
        logging.info('Request for hourly read from application cache')
    
    return data;

@weather.route("/daily")
@caching(60 * 24)
def daily():
    
    if request.cacheable == True:
        data = open_weather_map.daily()
        request.cache.write(data)

    else:
        data = request.cache.read()
        logging.info('Request for daily read from application cache')
    
    return data;
