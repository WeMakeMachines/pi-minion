from flask import request

from config import BaseConfig
from services import CachedOpenWeatherMap
from helpers import Units


class WeatherParams:
    @staticmethod
    def __get_units(arg):
        if arg == Units.IMPERIAL.value:
            return Units.IMPERIAL
        else:
            return Units.METRIC

    def __init__(self):
        self.speed_units = WeatherParams.__get_units(request.args.get("speed"))
        self.temperature_units = WeatherParams.__get_units(request.args.get("temp"))
        self.latitude = request.args.get("lat")
        self.longitude = request.args.get("long")
        self.nocache = request.args.get("nocache")


def open_weather_map():
    weather_params = WeatherParams()
    cache_key = f"${weather_params.latitude}{weather_params.longitude}"

    return CachedOpenWeatherMap(
        api_key=BaseConfig.OPEN_WEATHER_MAP_API_KEY,
        base_units=BaseConfig.BASE_UNITS,
        speed_units=weather_params.speed_units,
        temperature_units=weather_params.temperature_units,
        latitude=weather_params.latitude,
        longitude=weather_params.longitude,
        nocache=weather_params.nocache,
        cache_key=cache_key,
        language=BaseConfig.LANGUAGE
    )


def open_weather_map_now():
    return open_weather_map().now()


def open_weather_map_hourly():
    return open_weather_map().hourly()


def open_weather_map_daily():
    return open_weather_map().daily()
