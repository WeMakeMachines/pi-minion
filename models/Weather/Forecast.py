class Forecast(dict):
    def __init__(self, main: str, description: str):
        self.main = main
        self.description = description
        dict.__init__(self, main=self.main, description=self.description)
