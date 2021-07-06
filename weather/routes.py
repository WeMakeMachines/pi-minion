import logging
import json

from config import BaseConfig
from flask import Blueprint, request
from services import OpenWeatherMap
from middleware import Cacheable, set_caching_properties

logging.basicConfig(filename="pinion.weather.info.log", level=logging.INFO, format="%(asctime)s:%(message)s")

open_weather_map = OpenWeatherMap(BaseConfig.OPEN_WEATHER_MAP_API_KEY, BaseConfig.LATITUDE, BaseConfig.LONGITUDE)

weather = Blueprint("weather", __name__)


def __handle_caching_props(request, get_api_data):
    response_data = {}

    if request.cacheable == Cacheable.FALSE:
        cache = request.cache.read()
        response_data['cache_timestamp'] = cache['cache_timestamp']
        response_data['data'] = cache['cache']
        logging.info("Request for data read from application cache")

    else:
        response_data['data'] = get_api_data()

    if request.cacheable == Cacheable.TRUE:
        request.cache.write(response_data['data'])

    return response_data


@weather.route("/now")
def now():
    return open_weather_map.now()


@weather.route("/hourly")
@set_caching_properties(60)
def hourly():
    hourly_data = __handle_caching_props(request, open_weather_map.hourly)
    return json.dumps(hourly_data)


@weather.route("/daily")
@set_caching_properties(60 * 24)
def daily():
    daily_data = __handle_caching_props(request, open_weather_map.daily)
    return json.dumps(daily_data)
