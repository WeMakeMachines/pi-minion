from helpers import CacheExpiresAfter, Units
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')


def handle_cache_expires_after():
    try:
        if CacheExpiresAfter(config["cache"]["cache_expires_after"]) is CacheExpiresAfter.DISABLE:
            return CacheExpiresAfter.DISABLE

        if CacheExpiresAfter(config["cache"]["cache_expires_after"]) is CacheExpiresAfter.TODAY:
            return CacheExpiresAfter.TODAY

    except:
        return int(config["cache"]["cache_expires_after"])


class BaseConfigError(Exception):
    pass


class BaseConfig:
    OPEN_WEATHER_MAP_API_KEY = config["api"]["open_weather_map_key"]
    LATITUDE = config["general"]["latitude"]
    LONGITUDE = config["general"]["longitude"]
    CACHE_EXPIRES_AFTER = handle_cache_expires_after()
    DEFAULT_BASE_UNITS = Units.METRIC
    BASE_UNITS = DEFAULT_BASE_UNITS if config["general"]["base_units"] is None else Units(
        config["general"]["base_units"])
    DEFAULT_LANGUAGE = "en"
    LANGUAGE = DEFAULT_LANGUAGE if config["general"]["language"] is None else config["general"]["language"]
    MEMCACHED_SERVER = config["cache"]["memcached"]


if BaseConfig.OPEN_WEATHER_MAP_API_KEY is None:
    raise BaseConfigError("OPEN_WEATHER_MAP_API_KEY is missing")
