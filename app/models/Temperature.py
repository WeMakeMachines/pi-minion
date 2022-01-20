from app.helpers.units import Units


class Temperature:
    def __init__(self, units: Units, actual: float, feels_like: float = None):
        self.units = units.temperature()
        self.actual = actual
        self.feels_like = feels_like
