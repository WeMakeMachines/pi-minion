import requests
import json

from helpers import Units
from .mappers import Mapper, MapperUnits


# Interfaces with the OpenWeatherMap API
# Docs: https://openweathermap.org/api/one-call-api
class OpenWeatherMap:
    base_url = "https://api.openweathermap.org"
    one_call_route = "data/2.5/onecall"

    def __init__(self, api_key: str, latitude: float, longitude: float, base_units: Units):
        self.api_key = api_key
        self.latitude = latitude
        self.longitude = longitude
        self.base_units = base_units

    @staticmethod
    def get_json_from_request(url):
        response = requests.get(url)
        return json.loads(response.text)

    def now(self, speed_units: Units, temperature_units: Units):
        url = f"{self.base_url}/{self.one_call_route}?lat={self.latitude}&lon={self.longitude}&appid={self.api_key}&units={self.base_units.value}&exclude=minutely,hourly,daily,alerts"
        json_response = OpenWeatherMap.get_json_from_request(url)
        mapped = Mapper(MapperUnits(
            base_units=self.base_units,
            speed_units=speed_units,
            temperature_units=temperature_units))

        return mapped.map_now(json_response["current"])

    def hourly(self, speed_units: Units, temperature_units: Units):
        url = f"{self.base_url}/{self.one_call_route}?lat={self.latitude}&lon={self.longitude}&appid={self.api_key}&units={self.base_units.value}&exclude=current,minutely,daily,alerts"
        json_response = OpenWeatherMap.get_json_from_request(url)
        mapped = Mapper(MapperUnits(
            base_units=self.base_units,
            speed_units=speed_units,
            temperature_units=temperature_units))

        return mapped.map_hourly(json_response["hourly"])

    def daily(self, speed_units: Units, temperature_units: Units):
        url = f"{self.base_url}/{self.one_call_route}?lat={self.latitude}&lon={self.longitude}&appid={self.api_key}&units={self.base_units.value}&exclude=current,minutely,hourly,alerts"
        json_response = OpenWeatherMap.get_json_from_request(url)
        mapped = Mapper(MapperUnits(
            base_units=self.base_units,
            speed_units=speed_units,
            temperature_units=temperature_units))

        return mapped.map_daily(json_response["daily"])
