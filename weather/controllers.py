from flask import request

from config import BaseConfig
from services import CachedOpenWeatherMap
from helpers import CacheExpiresAfter
from .parameters import ExtractCacheParamsFromRequest, ExtractWeatherParamsFromRequest


def open_weather_map():
    weather_params = ExtractWeatherParamsFromRequest(request)
    cache_params = ExtractCacheParamsFromRequest(request)
    cache_key = f"{weather_params.latitude}{weather_params.longitude}"

    return CachedOpenWeatherMap(
        api_key=BaseConfig.OPEN_WEATHER_MAP_API_KEY,
        base_units=BaseConfig.BASE_UNITS,
        speed_units=weather_params.speed_units,
        temperature_units=weather_params.temperature_units,
        latitude=weather_params.latitude,
        longitude=weather_params.longitude,
        cache_expires_after=CacheExpiresAfter.DISABLE if cache_params.nocache else BaseConfig.CACHE_EXPIRES_AFTER,
        cache_key=cache_key,
        language=BaseConfig.LANGUAGE,
        memcached_url=BaseConfig.MEMCACHED_URL
    )


def open_weather_map_now():
    return open_weather_map().now()


def open_weather_map_hourly():
    return open_weather_map().hourly()


def open_weather_map_daily():
    return open_weather_map().daily()
