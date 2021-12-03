class Forecast(dict):
    def __init__(self, main: str, text: str):
        self.main = main.capitalize()
        self.text = text.capitalize()
        dict.__init__(self, main=self.main, text=self.text)
