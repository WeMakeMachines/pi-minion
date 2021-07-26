from config import BaseConfig
from flask import request
from services import OpenWeatherMap
from helpers import Units

open_weather_map = OpenWeatherMap(
    api_key=BaseConfig.OPEN_WEATHER_MAP_API_KEY,
    base_units=BaseConfig.BASE_UNITS
)


class WeatherArgs:
    def __init__(self):
        self.speed_units = WeatherArgs.__get_units(request.args.get('speed'))
        self.temperature_units = WeatherArgs.__get_units(request.args.get('temp'))
        self.latitude = request.args.get('lat')
        self.longitude = request.args.get('long')

    @staticmethod
    def __get_units(arg):
        if arg == Units.IMPERIAL.value:
            return Units.IMPERIAL
        else:
            return Units.METRIC


def get_units_from_args(api_call):
    weather_args = WeatherArgs()
    return api_call(speed_units=weather_args.speed_units, temperature_units=weather_args.temperature_units, latitude=weather_args.latitude, longitude=weather_args.longitude)


def open_weather_map_now():
    return get_units_from_args(open_weather_map.now)


def open_weather_map_hourly():
    return get_units_from_args(open_weather_map.hourly)


def open_weather_map_daily():
    return get_units_from_args(open_weather_map.daily)
