import requests
import json

from typing import List

from .mappers import Mapper
from .models import ReverseGeocodingLocation


class OpenWeatherMapGeocodingError(Exception):
    pass


# Interfaces with the OpenWeatherMap Geocoding API
# Docs: https://openweathermap.org/api/geocoding-api
class OpenWeatherMapGeocoding:
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

    def call_reverse_geocoding(self):
        try:
            response = requests.get(self.url_reverse)
            data = json.loads(response.text)
            reverse_geocoding_locations: List[ReverseGeocodingLocation] = [ReverseGeocodingLocation(**item) for item in
                                                                           data]
            return reverse_geocoding_locations
        except requests.ConnectionError:
            raise OpenWeatherMapGeocodingError("Connection Error")

    def call(self):
        return self.call_reverse_geocoding()

    def reverse_location(self):
        return self.mapper.map_reverse_location(self.raw_response)
