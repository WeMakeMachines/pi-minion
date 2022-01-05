class Clouds(dict):
    def __init__(self, cover: int, precipitation: float):
        self.cover = cover
        self.precipitation = precipitation
        dict.__init__(self, cover=self.cover, precipitation=self.precipitation)
