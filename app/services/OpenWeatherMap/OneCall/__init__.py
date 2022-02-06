import requests
import json

from app.utils.units import Units
from .models import OneCall
from .mappers import Mapper


class OpenWeatherMapOneCallError(Exception):
    pass


# Interfaces with the OpenWeatherMap One Call API
# Docs: https://openweathermap.org/api/one-call-api
class OpenWeatherMapOneCall:
    base_url = "https://api.openweathermap.org/data/2.5/onecall"

    def __init__(
            self,
            api_key: str,
            latitude: float,
            longitude: float,
            language: str,
            base_units: Units,
            speed_units: Units,
            temperature_units: Units,
    ):
        self.api_key = api_key
        self.base_units = base_units
        self.speed_units = speed_units
        self.temperature_units = temperature_units
        self.latitude = latitude
        self.longitude = longitude
        self.language = language
        self.url = f"{self.base_url}?lat={latitude}&lon={longitude}&appid={api_key}&units={base_units.value}&lang={language}&exclude=minutely"
        self.raw_response = {}
        self.mapper = Mapper(
            base_units=self.base_units,
            speed_units=self.speed_units,
            temperature_units=self.temperature_units
        )

    def call(self):
        try:
            response = requests.get(self.url)
            data = json.loads(response.text)
            one_call: OneCall = data
            return one_call

        except requests.ConnectionError:
            raise OpenWeatherMapOneCallError("Connection Error")

    def now(self):
        return self.mapper.map_now(self.raw_response["current"])

    def hourly(self):
        return self.mapper.map_hourly(self.raw_response["hourly"])

    def daily(self):
        return self.mapper.map_daily(self.raw_response["daily"])

    def alerts(self):
        if hasattr(self.raw_response, "alerts"):
            return self.mapper.map_alerts(self.raw_response["alerts"])

        return []
