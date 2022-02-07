from app.utils.MemcachedCacher import CacheBehaviour
from app.utils.units import Units
from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")


class BaseConfigError(Exception):
    pass


def handle_cache_behaviour():
    try:
        if CacheBehaviour(config["cache"]["cache_behaviour"]) is CacheBehaviour.DISABLE:
            print("Caching is disabled")
            return CacheBehaviour.DISABLE

        if (
            CacheBehaviour(config["cache"]["cache_behaviour"])
            is CacheBehaviour.RENEW_DAILY
        ):
            print("Caching is set to renew daily")
            return CacheBehaviour.RENEW_DAILY

    except:
        return CacheBehaviour.USER_SPECIFIED


class BaseConfig:
    OPEN_WEATHER_MAP_API_KEY = config["api"]["open_weather_map_key"]
    LATITUDE = config.getfloat("general", "latitude")
    LONGITUDE = config.getfloat("general", "longitude")
    CACHE_BEHAVIOUR = handle_cache_behaviour()
    CACHE_EXPIRES_AFTER = config.getint("cache", "cache_expires_after") or 0
    DEFAULT_BASE_UNITS = Units.METRIC
    BASE_UNITS = (
        DEFAULT_BASE_UNITS
        if config["general"]["base_units"] is None
        else Units(config["general"]["base_units"])
    )
    DEFAULT_LANGUAGE = "en"
    LANGUAGE = (
        DEFAULT_LANGUAGE
        if config["general"]["language"] is None
        else config["general"]["language"]
    )
    MEMCACHED_SERVER = config["cache"]["memcached"]


if BaseConfig.OPEN_WEATHER_MAP_API_KEY is None:
    raise BaseConfigError("OPEN_WEATHER_MAP_API_KEY is missing")
