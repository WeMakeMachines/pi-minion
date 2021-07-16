from models.Weather import Wind
from helpers import Units, Speed


# by default, OpenWeatherMap will return m/s for metric values
# so we convert m/s to km/h
class NormalisedWind(Wind):
    def __init__(self, units: Units, speed: float, degrees: int, gust: float = None):
        if units is Units.METRIC:
            speed = Speed.metres_per_second_to_km_per_hour(speed)

            if gust is not None:
                gust = Speed.metres_per_second_to_km_per_hour(gust)

        super().__init__(units, speed, degrees, gust)
