from fastapi import Request
from config import BaseConfig
from app.services.CachedOpenWeatherMap.CachedOpenWeatherMapOneCall import (
    CachedOpenWeatherMapOneCall,
)
from app.services.CachedOpenWeatherMap.CachedOpenWeatherMapReverseGeocoding import (
    CachedOpenWeatherMapReverseGeocoding,
)
from app.utils.CacheRequest.types import CacheBehaviour
from app.utils.request import (
    ExtractCacheBehaviourFromRequestState,
    ExtractUnitsFromRequestState,
)


def open_weather_map(request: Request, now: str, hourly: str, daily: str, alerts: str):
    cache_behaviour = ExtractCacheBehaviourFromRequestState(request)
    units = ExtractUnitsFromRequestState(request)
    _open_weather_map_one_call = CachedOpenWeatherMapOneCall(
        api_key=BaseConfig.OPEN_WEATHER_MAP_API_KEY,
        base_units=BaseConfig.BASE_UNITS,
        speed_units=units.speed_units,
        temperature_units=units.temperature_units,
        latitude=BaseConfig.LATITUDE,
        longitude=BaseConfig.LONGITUDE,
        language=BaseConfig.LANGUAGE,
        cache_expires_after=BaseConfig.CACHE_EXPIRES_AFTER,
        cache_behaviour=CacheBehaviour.DISABLE
        if cache_behaviour.nocache
        else BaseConfig.CACHE_BEHAVIOUR,
        cache_key="open.weather.map.one.call",
        memcached_server=BaseConfig.MEMCACHED_SERVER,
    )
    _open_weather_map_geocoding = CachedOpenWeatherMapReverseGeocoding(
        api_key=BaseConfig.OPEN_WEATHER_MAP_API_KEY,
        latitude=BaseConfig.LATITUDE,
        longitude=BaseConfig.LONGITUDE,
        language=BaseConfig.LANGUAGE,
        cache_behaviour=CacheBehaviour.CACHE_ONCE,
        cache_key="open.weather.map.geocoding",
        memcached_server=BaseConfig.MEMCACHED_SERVER,
    )

    data = _open_weather_map_geocoding.reverse_location()

    if now is not None:
        data["now"] = _open_weather_map_one_call.now()
    if hourly is not None:
        data["hourly"] = _open_weather_map_one_call.hourly()
    if daily is not None:
        data["daily"] = _open_weather_map_one_call.daily()
    if alerts is not None:
        _alerts = _open_weather_map_one_call.alerts()
        if len(_alerts) != 0:
            data["alerts"] = _alerts
    if _open_weather_map_one_call.cache.cached is True:
        data["cache_timestamp"] = _open_weather_map_one_call.cache.cache_timestamp
    return data
