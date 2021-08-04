class Clouds(dict):
    @staticmethod
    def __describe_cloud_cover(cloud_cover):
        description = ["clear", "mostly clear", "mostly clear", "partly cloudy", "partly cloudy", "mostly cloudy",
                       "mostly cloudy", "overcast"]

        pick = int((99 if cloud_cover >= 100 else cloud_cover) / (100 / 8))

        return description[pick]

    def __init__(self, cover: int):
        self.cover = cover
        self.description = self.__describe_cloud_cover(self.cover)
        dict.__init__(self, cover=self.cover, description=self.description)
