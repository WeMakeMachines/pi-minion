from dotenv import dotenv_values
from helpers import CacheValidity, Units

config = dotenv_values(".env")


class BaseConfigError(Exception):
    pass


class BaseConfig:
    OPEN_WEATHER_MAP_API_KEY = config.get("OPEN_WEATHER_MAP_API_KEY")
    LATITUDE = config.get("LATITUDE")
    LONGITUDE = config.get("LONGITUDE")
    CACHE_VALIDITY = CacheValidity.DISABLE if config.get(
        "CACHE_VALIDITY") is None else CacheValidity(config.get("CACHE_VALIDITY"))
    DEFAULT_BASE_UNITS = Units.METRIC
    BASE_UNITS = DEFAULT_BASE_UNITS if config.get("BASE_UNITS") is None else Units(config.get("BASE_UNITS"))
    DEFAULT_LANGUAGE = "en"
    LANGUAGE = DEFAULT_LANGUAGE if config.get("LANGUAGE") is None else config.get("LANGUAGE")


if BaseConfig.OPEN_WEATHER_MAP_API_KEY is None:
    raise BaseConfigError("OPEN_WEATHER_MAP_API_KEY is missing")
