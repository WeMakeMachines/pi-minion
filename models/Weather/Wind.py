from helpers import Units


class Wind(dict):
    @staticmethod
    def __describe_wind_direction(degrees):
        description = ["north", "north east", "east", "south east", "south", "south west", "west", "north west"]
        degrees_in_compass = 360
        cardinal_points = 8
        degrees_per_cardinal_points = degrees_in_compass / cardinal_points

        pick = int((degrees + degrees_per_cardinal_points / 2) / degrees_per_cardinal_points)

        return description[(pick % cardinal_points)]

    def __init__(self, units: Units, speed: float, degrees: int, gust: float = None):
        self.units = units.speed()
        self.speed = speed
        self.degrees = degrees
        self.gust = gust
        self.description = self.__describe_wind_direction(self.degrees)
        dict.__init__(self, speed=self.speed, degrees=self.degrees, gust=self.gust, description=self.description)
