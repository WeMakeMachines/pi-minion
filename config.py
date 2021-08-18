from dotenv import dotenv_values
from helpers import CacheExpiresAfter, Units

config = dotenv_values(".env")


def handle_cache_expires_after():
    try:
        if CacheExpiresAfter(config.get("CACHE_EXPIRES_AFTER")) is CacheExpiresAfter.DISABLE:
            return CacheExpiresAfter.DISABLE

        if CacheExpiresAfter(config.get("CACHE_EXPIRES_AFTER")) is CacheExpiresAfter.TODAY:
            return CacheExpiresAfter.TODAY

    except:
        return int(config.get("CACHE_EXPIRES_AFTER"))


class BaseConfigError(Exception):
    pass


class BaseConfig:
    OPEN_WEATHER_MAP_API_KEY = config.get("OPEN_WEATHER_MAP_API_KEY")
    LATITUDE = config.get("LATITUDE")
    LONGITUDE = config.get("LONGITUDE")
    CACHE_EXPIRES_AFTER = handle_cache_expires_after()
    DEFAULT_BASE_UNITS = Units.METRIC
    BASE_UNITS = DEFAULT_BASE_UNITS if config.get("BASE_UNITS") is None else Units(config.get("BASE_UNITS"))
    DEFAULT_LANGUAGE = "en"
    LANGUAGE = DEFAULT_LANGUAGE if config.get("LANGUAGE") is None else config.get("LANGUAGE")
    MEMCACHED_SERVER = config.get("MEMCACHED_SERVER")


if BaseConfig.OPEN_WEATHER_MAP_API_KEY is None:
    raise BaseConfigError("OPEN_WEATHER_MAP_API_KEY is missing")
