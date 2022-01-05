class Forecast(dict):
    def __init__(self, title: str, body: str):
        self.title = title.capitalize()
        self.body = body.capitalize()
        dict.__init__(self, title=self.title, body=self.body)
