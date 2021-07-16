import requests
import json

from helpers import Units
from .mappers import map_now, map_daily, map_hourly


# Interfaces with the OpenWeatherMap API
# Docs: https://openweathermap.org/api/one-call-api
class OpenWeatherMap:
    def __init__(self, api_key: str, latitude: float, longitude: float, units: Units = Units.METRIC):
        self.api_key = api_key
        self.latitude = latitude
        self.longitude = longitude
        self.units = units

    def now(self):
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/onecall?lat={self.latitude}&lon={self.longitude}&appid={self.api_key}&units={self.units.value}&exclude=minutely,hourly,daily,alerts")

        json_response = json.loads(response.text)
        now = json_response["current"]

        return map_now(now, self.units)

    def hourly(self):
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/onecall?lat={self.latitude}&lon={self.longitude}&appid={self.api_key}&units={self.units.value}&exclude=current,minutely,daily,alerts")

        json_response = json.loads(response.text)
        data = []

        for hour in json_response["hourly"]:
            data.append(map_hourly(hour, self.units))

        return data

    def daily(self):
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/onecall?lat={self.latitude}&lon={self.longitude}&appid={self.api_key}&units={self.units.value}&exclude=current,minutely,hourly,alerts")

        json_response = json.loads(response.text)
        data = []

        for day in json_response["daily"]:
            data.append(map_daily(day, self.units))

        return data
