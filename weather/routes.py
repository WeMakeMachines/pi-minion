import logging

from config import BaseConfig
from flask import abort, Blueprint, request
from services import Caching, OpenWeatherMap
from middleware import Cacheable, set_caching_properties

logging.basicConfig(filename="pinion.weather.info.log",level=logging.INFO, format="%(asctime)s:%(message)s")

open_weather_map = OpenWeatherMap(BaseConfig.OPEN_WEATHER_MAP_API_KEY, BaseConfig.LATITUDE, BaseConfig.LONGITUDE);

weather = Blueprint("weather", __name__, url_prefix="/weather")

def __handle_caching_props(request, get_data):
    
    if request.cacheable == Cacheable.FALSE:
        data = request.cache.read()
        logging.info("Request for data read from application cache")
    
    else:
        data = get_data()
    
    if request.cacheable == True:
        request.cache.write(data)

    return data;

@weather.route("/now")
def now():
    return open_weather_map.now()

@weather.route("/hourly")
@set_caching_properties(60)
def hourly():
    return __handle_caching_props(request, open_weather_map.hourly)

@weather.route("/daily")
@set_caching_properties(60 * 24)
def daily():
    return __handle_caching_props(request, open_weather_map.daily)
