class Sun(dict):
    def __init__(self, sunrise: int, sunset: int, uv: float):
        self.sunrise = sunrise
        self.sunset = sunset
        self.uv = uv
        dict.__init__(self, sunrise=self.sunrise, sunset=self.sunset, uv=self.uv)
