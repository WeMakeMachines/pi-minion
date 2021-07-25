from config import BaseConfig
from flask import Blueprint, request
from werkzeug.datastructures import OrderedMultiDict
from middleware import cache_api_response, Valid
from .controllers import open_weather_map_now, open_weather_map_daily, open_weather_map_hourly

weather = Blueprint("weather", __name__)


def normalise_weather_params(function):

    def decorator():
        units_params = ["speed", "temperature"]
        ordered_params = {}

        for param in units_params:
            client_value = request.args.get(param)

            if client_value is not None:
                ordered_params[param] = client_value
            else:
                ordered_params[param] = BaseConfig.BASE_UNITS.value

        request.parameter_storage_class = OrderedMultiDict
        request.args = ordered_params

        return function()

    return decorator


@weather.before_request
@normalise_weather_params
def __normalise_weather_params():
    pass


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
