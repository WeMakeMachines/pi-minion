from helpers import Units


class Temperature(dict):
    def __init__(self, units: Units, actual: float, feels_like: float = None):
        self.units = units.temperature()
        self.actual = actual
        self.feels_like = feels_like
        dict.__init__(self, units=self.units.value, actual=self.actual, feels_like=self.feels_like)
