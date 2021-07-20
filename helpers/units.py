from enum import Enum, unique


@unique
class Units(Enum):
    IMPERIAL = "imperial"
    METRIC = "metric"

    def speed(self):
        if self.value is self.IMPERIAL.value:
            return SpeedUnits.MILES_PER_HOUR

        if self.value == self.METRIC.value:
            return SpeedUnits.KILOMETRES_PER_HOUR

    def temperature(self):
        if self.value is self.IMPERIAL.value:
            return TemperatureUnits.FAHRENHEIT

        if self.value is self.METRIC.value:
            return TemperatureUnits.CELSIUS


@unique
class SpeedUnits(Enum):
    MILES_PER_HOUR = "miles/h"
    KILOMETRES_PER_HOUR = "km/h"

    @staticmethod
    def metres_per_second_to_km_per_hour(value: float):
        return round(value * 3.599712, 1)

    @staticmethod
    def as_imperial(value: float):
        if value is None:
            return value

        return round(value * 0.621477, 1)

    @staticmethod
    def as_metric(value: float):
        if value is None:
            return value

        return round(value * 1.609071, 1)


@unique
class TemperatureUnits(Enum):
    FAHRENHEIT = "fahrenheit"
    CELSIUS = "celsius"

    @staticmethod
    def as_imperial(value):
        if value is None:
            return value

        return round((value - 32) * 5 / 9, 1)

    @staticmethod
    def as_metric(value):
        if value is None:
            return value

        return round((value * 9 / 5) + 32, 1)
