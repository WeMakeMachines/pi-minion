from flask import Blueprint
from middleware import cache_api_response, Valid
from .controllers import open_weather_map_now, open_weather_map_daily, open_weather_map_hourly

weather = Blueprint("weather", __name__)


@weather.route("/now")
@cache_api_response(Valid.THIS_HOUR, open_weather_map_now)
def now(response):
    return response


@weather.route("/hourly")
@cache_api_response(Valid.THIS_HOUR, open_weather_map_hourly)
def hourly(response):
    return response


@weather.route("/daily")
@cache_api_response(Valid.TODAY, open_weather_map_daily)
def daily(response):
    return response
