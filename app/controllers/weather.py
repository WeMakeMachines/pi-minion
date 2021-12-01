from fastapi import Request
from config import BaseConfig
from app.services.CachedOpenWeatherMap import CachedOpenWeatherMap
from app.helpers.cache import CacheExpiresAfter
from app.helpers.request import ExtractCacheFromRequestState, ExtractUnitsFromRequestState, ExtractLocationFromRequestState


def open_weather_map(request: Request):
    cache = ExtractCacheFromRequestState(request)
    units = ExtractUnitsFromRequestState(request)
    location = ExtractLocationFromRequestState(request)
    cache_key = f"{location.latitude}{location.longitude}"

    return CachedOpenWeatherMap(
        api_key=BaseConfig.OPEN_WEATHER_MAP_API_KEY,
        base_units=BaseConfig.BASE_UNITS,
        speed_units=units.speed_units,
        temperature_units=units.temperature_units,
        latitude=location.latitude,
        longitude=location.longitude,
        cache_expires_after=CacheExpiresAfter.DISABLE if cache.nocache else BaseConfig.CACHE_EXPIRES_AFTER,
        cache_key=cache_key,
        language=BaseConfig.LANGUAGE,
        memcached_server=BaseConfig.MEMCACHED_SERVER
    )


def open_weather_map_now(request: Request):
    return open_weather_map(request).now()


def open_weather_map_hourly(request: Request):
    return open_weather_map(request).hourly()


def open_weather_map_daily(request: Request):
    return open_weather_map(request).daily()
