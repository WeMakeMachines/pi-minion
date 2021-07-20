from models.Weather import Temperature, Wind
from helpers import Units, SpeedUnits, TemperatureUnits


class ConvertedTemperature(Temperature):
    def __init__(self, base_units: Units, units: Units, actual: float, feels_like: float = None):
        if base_units is not units:
            if units is Units.IMPERIAL:
                actual = TemperatureUnits.as_metric(actual)
                feels_like = TemperatureUnits.as_metric(feels_like)

            if units is Units.METRIC:
                actual = TemperatureUnits.as_imperial(actual)
                feels_like = TemperatureUnits.as_imperial(feels_like)

        super().__init__(units, actual, feels_like)


class ConvertedWind(Wind):
    def __init__(self, base_units: Units, units: Units, speed: float, degrees: int, gust: float = None):
        # by default, OpenWeatherMap will return m/s for metric values
        # so we convert m/s to km/h
        if base_units is Units.METRIC:
            speed = SpeedUnits.metres_per_second_to_km_per_hour(speed)

            if gust is not None:
                gust = SpeedUnits.metres_per_second_to_km_per_hour(gust)

        if base_units is not units:
            if units is Units.IMPERIAL:
                speed = SpeedUnits.as_imperial(speed)
                gust = TemperatureUnits.as_imperial(gust)

            if units is Units.METRIC:
                speed = SpeedUnits.as_metric(speed)
                gust = TemperatureUnits.as_metric(gust)

        super().__init__(units, speed, degrees, gust)
