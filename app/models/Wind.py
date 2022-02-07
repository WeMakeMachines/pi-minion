from typing import Optional

from app.utils.units import SpeedUnits


class Wind:
    @staticmethod
    def describe_wind_direction(degrees: int):
        description = [
            "north",
            "north east",
            "east",
            "south east",
            "south",
            "south west",
            "west",
            "north west",
        ]
        degrees_in_compass = 360
        cardinal_points = len(description)
        degrees_per_cardinal_points = degrees_in_compass / cardinal_points

        pick = int(
            (degrees + degrees_per_cardinal_points / 2) / degrees_per_cardinal_points
        )

        return description[(pick % cardinal_points)]

    @staticmethod
    def calc_beaufort_scale(speed: float, units: SpeedUnits):
        if units is SpeedUnits.KILOMETRES_PER_HOUR:
            speed_as_miles_per_hour = round(SpeedUnits.as_imperial(speed))
        else:
            speed_as_miles_per_hour = round(speed)

        # Information taken from https://en.wikipedia.org/wiki/Beaufort_scale
        if 1 <= speed_as_miles_per_hour <= 3:
            return 1
        if 4 <= speed_as_miles_per_hour <= 7:
            return 2
        if 8 <= speed_as_miles_per_hour <= 12:
            return 3
        if 13 <= speed_as_miles_per_hour <= 18:
            return 4
        if 19 <= speed_as_miles_per_hour <= 24:
            return 5
        if 25 <= speed_as_miles_per_hour <= 31:
            return 6
        if 32 <= speed_as_miles_per_hour <= 38:
            return 7
        if 39 <= speed_as_miles_per_hour <= 46:
            return 8
        if 47 <= speed_as_miles_per_hour <= 54:
            return 9
        if 55 <= speed_as_miles_per_hour <= 63:
            return 10
        if 64 <= speed_as_miles_per_hour <= 72:
            return 11
        if 73 <= speed_as_miles_per_hour:
            return 12

        return 0

    def __init__(
        self, units: SpeedUnits, speed: float, degrees: int, gust: Optional[float]
    ):
        self.units = units
        self.speed = speed
        self.degrees = degrees
        self.direction = self.describe_wind_direction(self.degrees)
        self.beaufort = self.calc_beaufort_scale(self.speed, self.units)
        if gust is not None:
            self.gust = gust
