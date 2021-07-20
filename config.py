from dotenv import dotenv_values
from helpers import Units

config = dotenv_values(".env")


class BaseConfig():
    OPEN_WEATHER_MAP_API_KEY = config["OPEN_WEATHER_MAP_API_KEY"]
    LATITUDE = config["LATITUDE"]
    LONGITUDE = config["LONGITUDE"]
    DISABLE_CACHING = True if config.get("DISABLE_CACHING") == "True" else False
    BASE_UNITS = Units.IMPERIAL if config.get("DEFAULT_UNITS") == Units.IMPERIAL.value else Units.METRIC
