import requests
import json

from helpers import Units
from .mappers import Mapper, MapperUnits


class OpenWeatherMapError(Exception):
    pass


# Interfaces with the OpenWeatherMap API
# Docs: https://openweathermap.org/api/one-call-api
class OpenWeatherMap:
    base_url = "https://api.openweathermap.org"
    one_call_route = "data/2.5/onecall"

    def __init__(
            self,
            api_key: str,
            base_units: Units,
            speed_units: Units,
            temperature_units: Units,
            latitude: float,
            longitude: float,
            language: str
    ):
        if api_key is None:
            raise OpenWeatherMapError("OpenWeatherMap API Key not found")

        self.api_key = api_key
        self.base_units = base_units
        self.speed_units = speed_units
        self.temperature_units = temperature_units
        self.latitude = latitude
        self.longitude = longitude
        self.url = f"{self.base_url}/{self.one_call_route}?lat={latitude}&lon={longitude}&appid={api_key}&units={base_units.value}&lang={language}"
        self.raw_response = {}
        self.parsed_data = {
            "location": {
                "lat": self.latitude,
                "long": self.longitude
            }
        }

    def call(self):
        response = requests.get(self.url)
        return json.loads(response.text)

    def mapper(self):
        return Mapper(
            units=MapperUnits(
                base_units=self.base_units,
                speed_units=self.speed_units,
                temperature_units=self.temperature_units
            )
        )

    def now(self):
        self.parsed_data.update(self.mapper().map_now(self.raw_response["current"]))
        return self.parsed_data

    def hourly(self):
        self.parsed_data.update(self.mapper().map_hourly(self.raw_response["hourly"]))
        return self.parsed_data

    def daily(self):
        self.parsed_data.update(self.mapper().map_daily(self.raw_response["daily"]))
        return self.parsed_data
