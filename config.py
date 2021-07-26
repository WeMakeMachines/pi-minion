from dotenv import dotenv_values
from helpers import CacheValidity, Units

config = dotenv_values(".env")


class BaseConfig:
    OPEN_WEATHER_MAP_API_KEY = config["OPEN_WEATHER_MAP_API_KEY"]
    LATITUDE = config["LATITUDE"]
    LONGITUDE = config["LONGITUDE"]
    CACHE_VALIDITY = CacheValidity(config.get("CACHE_VALIDITY")) if config.get("CACHE_VALIDITY") is not None else CacheValidity.DISABLE
    BASE_UNITS = Units.IMPERIAL if config.get("DEFAULT_UNITS") == Units.IMPERIAL.value else Units.METRIC
