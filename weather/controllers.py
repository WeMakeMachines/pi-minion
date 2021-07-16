from config import BaseConfig
from flask import request
from services import OpenWeatherMap
from helpers import Units

open_weather_map = OpenWeatherMap(
    BaseConfig.OPEN_WEATHER_MAP_API_KEY,
    BaseConfig.LATITUDE,
    BaseConfig.LONGITUDE,
    BaseConfig.DEFAULT_UNITS
)


def get_units_from_args(api_call):
    arg_units = request.args.get('units')
    units = None

    if arg_units == Units.METRIC.value:
        units = Units.METRIC
    if arg_units == Units.IMPERIAL.value:
        units = Units.IMPERIAL

    return api_call(units)


def open_weather_map_now():
    return get_units_from_args(open_weather_map.now)


def open_weather_map_hourly():
    return get_units_from_args(open_weather_map.hourly)


def open_weather_map_daily():
    return get_units_from_args(open_weather_map.daily)
