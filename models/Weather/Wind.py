from typing import Tuple, overload

class Wind(dict):
    def __init__(self, **kwargs):
        self.speed = kwargs.get('speed')
        self.degrees = kwargs.get('degrees')
        self.gust = kwargs.get('gust')
        self.description = self.__describe_wind_direction(self.degrees)
        dict.__init__(self, speed = self.speed, degrees = self.degrees, gust = self.gust, description = self.description)
    
    def __describe_wind_direction(self, degrees):
        description = ["north", "north east", "east", "south east", "south", "south west", "west", "north west"]
        degrees_in_compass = 360
        cardinal_points = 8
        degrees_per_cardinal_points = 360 / cardinal_points
        
        pick = int((degrees + degrees_per_cardinal_points / 2) / degrees_per_cardinal_points)
        
        return description[(pick % cardinal_points)]
