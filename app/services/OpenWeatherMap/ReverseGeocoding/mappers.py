from app.models.Location import Location
from .models import ReverseGeocodingLocation


class Mapper:
    def __init__(self, language=str):
        self.language = language

    def __map_reverse_location(self, location: ReverseGeocodingLocation):
        return {
            "location": Location(
                lat=location["lat"],
                long=location["lon"],
                name=location["local_names"][self.language],
            )
        }

    def map_reverse_location(self, locations):
        return self.__map_reverse_location(location=locations[0])
