import requests
import json

from app.helpers.units import Units
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
        self.api_key = api_key
        self.base_units = base_units
        self.speed_units = speed_units
        self.temperature_units = temperature_units
        self.latitude = latitude
        self.longitude = longitude
        self.url = f"{self.base_url}/{self.one_call_route}?lat={latitude}&lon={longitude}&appid={api_key}&units={base_units.value}&lang={language}&exclude=minutely"
        self.raw_response = {}
        self.location = {
            "location": {
                "lat": self.latitude,
                "long": self.longitude
            }
        }

    def call(self):
        try:
            response = requests.get(self.url)
            return json.loads(response.text)
        except requests.ConnectionError:
            raise OpenWeatherMapError("Connection Error")

    def mapper(self):
        return Mapper(
            units=MapperUnits(
                base_units=self.base_units,
                speed_units=self.speed_units,
                temperature_units=self.temperature_units
            )
        )

    def now(self):
        return self.mapper().map_now(self.raw_response["current"])

    def hourly(self):
        return self.mapper().map_hourly(self.raw_response["hourly"])

    def daily(self):
        return self.mapper().map_daily(self.raw_response["daily"])
