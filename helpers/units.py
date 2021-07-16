from enum import Enum, unique


@unique
class Units(Enum):
    IMPERIAL = "imperial"
    METRIC = "metric"

    def speed(self):
        if self.value is self.IMPERIAL.value:
            return Speed.MILES_PER_HOUR

        if self.value == self.METRIC.value:
            return Speed.KILOMETRES_PER_HOUR

    def temperature(self):
        if self.value is self.IMPERIAL.value:
            return Temperature.FAHRENHEIT

        if self.value is self.METRIC.value:
            return Temperature.CELSIUS


@unique
class Speed(Enum):
    KILOMETRES_PER_HOUR = "km/h"
    MILES_PER_HOUR = "miles/h"

    @staticmethod
    def metres_per_second_to_km_per_hour(value):
        return round(value * 3.599712, 1)


@unique
class Temperature(Enum):
    CELSIUS = "celsius"
    FAHRENHEIT = "fahrenheit"
