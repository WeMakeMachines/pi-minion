class Sun(dict):
    def __init__(self, sunrise: int, sunset: int):
        self.sunrise = sunrise
        self.sunset = sunset
        dict.__init__(self, sunrise=self.sunrise, sunset=self.sunset)
