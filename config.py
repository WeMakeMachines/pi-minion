from dotenv import dotenv_values

config = dotenv_values(".env")

class BaseConfig():
    OPEN_WEATHER_MAP_API_KEY = config["OPEN_WEATHER_MAP_API_KEY"]
    LATITUDE = config["LATITUDE"]
    LONGITUDE = config["LONGITUDE"]
