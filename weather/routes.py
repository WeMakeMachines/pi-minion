from flask import Blueprint
from .middleware import normalise_weather_params
from .controllers import open_weather_map_now, open_weather_map_daily, open_weather_map_hourly

weather = Blueprint("weather", __name__)


@weather.before_request
@normalise_weather_params
def __normalise_weather_params():
    pass


@weather.route("/now")
def now():
    return open_weather_map_now()


@weather.route("/hourly")
def hourly():
    return open_weather_map_hourly()


@weather.route("/daily")
def daily():
    return open_weather_map_daily()
