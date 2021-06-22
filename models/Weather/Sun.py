class Sun(dict):
    def __init__(self, **kwargs):
        self.sunrise = kwargs.get('sunrise')
        self.sunset = kwargs.get('sunset')
        dict.__init__(self, sunrise = self.sunrise, sunset = self.sunset)
