class Clouds(dict):
    def __init__(self, cover: int):
        self.cover = cover
        dict.__init__(self, cover=self.cover)
