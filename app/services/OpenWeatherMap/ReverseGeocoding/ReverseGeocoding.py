import requests
import json

from .mappers import Mapper


class OpenWeatherMapReverseGeocodingError(Exception):
    pass


# Interfaces with the OpenWeatherMap ReverseGeocoding API
# Docs: https://openweathermap.org/api/geocoding-api
class OpenWeatherMapReverseGeocoding:
    base_url = "http://api.openweathermap.org/geo/1.0"

    def __init__(self, api_key: str, latitude: float, longitude: float, language: str):
        self.api_key = api_key
        self.latitude = latitude
        self.longitude = longitude
        self.language = language
        self.url = f"{self.base_url}/reverse?lat={latitude}&lon={longitude}&appid={api_key}&limit=1"
        self.response = []
        self.mapper = Mapper(language=self.language)

    def call(self):
        try:
            response = requests.get(self.url)
            data = json.loads(response.text)
            return data
        except requests.ConnectionError:
            raise OpenWeatherMapReverseGeocodingError("Connection Error")

    def reverse_location(self):
        return self.mapper.map_reverse_location(self.response)
