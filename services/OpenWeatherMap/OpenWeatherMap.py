import requests
import json

from helpers import Units
from .mappers import Mapper


# Interfaces with the OpenWeatherMap API
# Docs: https://openweathermap.org/api/one-call-api
class OpenWeatherMap:
    def __init__(self, api_key: str, latitude: float, longitude: float, default_units: Units = Units.METRIC):
        self.api_key = api_key
        self.latitude = latitude
        self.longitude = longitude
        self.default_units = default_units

    def now(self, units: Units = None):
        if units is None:
            units = self.default_units

        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/onecall?lat={self.latitude}&lon={self.longitude}&appid={self.api_key}&units={units.value}&exclude=minutely,hourly,daily,alerts")

        json_response = json.loads(response.text)
        now = json_response["current"]
        mapped = Mapper(units)

        return mapped.map_now(now)

    def hourly(self, units: Units = None):
        if units is None:
            units = self.default_units

        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/onecall?lat={self.latitude}&lon={self.longitude}&appid={self.api_key}&units={units.value}&exclude=current,minutely,daily,alerts")

        json_response = json.loads(response.text)
        mapped = Mapper(units)

        return mapped.map_hourly(json_response["hourly"])

    def daily(self, units: Units = None):
        if units is None:
            units = self.default_units

        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/onecall?lat={self.latitude}&lon={self.longitude}&appid={self.api_key}&units={units.value}&exclude=current,minutely,hourly,alerts")

        json_response = json.loads(response.text)
        mapped = Mapper(units)

        return mapped.map_daily(json_response["daily"])
