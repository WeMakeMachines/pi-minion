from fastapi import Request
from config import BaseConfig
from app.services.CachedOpenWeatherMapOneCall import CachedOpenWeatherMapOneCall
from app.helpers.cache import CacheExpiresAfter
from app.helpers.request import ExtractCacheFromRequestState, ExtractUnitsFromRequestState


def open_weather_map(request: Request, now: str, hourly: str, daily: str, alerts: str):
    cache = ExtractCacheFromRequestState(request)
    units = ExtractUnitsFromRequestState(request)
    cache_key = f"{BaseConfig.LATITUDE}{BaseConfig.LONGITUDE}"
    _open_weather_map = CachedOpenWeatherMapOneCall(
        api_key=BaseConfig.OPEN_WEATHER_MAP_API_KEY,
        base_units=BaseConfig.BASE_UNITS,
        speed_units=units.speed_units,
        temperature_units=units.temperature_units,
        latitude=BaseConfig.LATITUDE,
        longitude=BaseConfig.LONGITUDE,
        cache_expires_after=CacheExpiresAfter.DISABLE if cache.nocache else BaseConfig.CACHE_EXPIRES_AFTER,
        cache_key=cache_key,
        language=BaseConfig.LANGUAGE,
        memcached_server=BaseConfig.MEMCACHED_SERVER
    )

    data = {"location": _open_weather_map.location}
    if now is not None:
        data["now"] = _open_weather_map.now()
    if hourly is not None:
        data["hourly"] = _open_weather_map.hourly()
    if daily is not None:
        data["daily"] = _open_weather_map.daily()
    if alerts is not None:
        data["alerts"] = _open_weather_map.alerts()
    if _open_weather_map.cached is True:
        data["cache_timestamp"] = _open_weather_map.cache_timestamp
    return data
