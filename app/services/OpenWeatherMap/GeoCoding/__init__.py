import requests
import json

from .mappers import Mapper


class OpenWeatherMapGeoCodingError(Exception):
    pass


# Interfaces with the OpenWeatherMap GeoCoding API
# Docs: https://openweathermap.org/api/geocoding-api
class OpenWeatherMapGeoCoding:
    base_url = "http://api.openweathermap.org/geo/1.0"

    def __init__(
            self,
            api_key: str,
            latitude: float,
            longitude: float,
            language: str
    ):
        self.api_key = api_key
        self.latitude = latitude
        self.longitude = longitude
        self.language = language
        self.url_reverse = f"{self.base_url}/reverse?lat={latitude}&lon={longitude}&appid={api_key}&limit=1"
        self.raw_response = []
        self.mapper = Mapper(language=self.language)

    def call_reverse(self):
        try:
            response = requests.get(self.url_reverse)
            return json.loads(response.text)
        except requests.ConnectionError:
            raise OpenWeatherMapGeoCodingError("Connection Error")

    def call(self):
        return self.call_reverse()

    def reverse_location(self):
        return self.mapper.map_reverse_location(self.raw_response)
