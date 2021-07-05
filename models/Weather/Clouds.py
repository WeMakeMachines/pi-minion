class Clouds(dict):
    @staticmethod
    def __describe_cloud_cover(cloud_cover):
        description = ["clear", "mostly clear", "mostly clear", "partly cloudy", "partly cloudy", "mostly cloudy",
                       "mostly cloudy", "overcast"]

        pick = int((99 if cloud_cover >= 100 else cloud_cover) / (100 / 8))

        return description[pick]

    def __init__(self, cloud_cover: int):
        self.cloud_cover = cloud_cover
        self.description = self.__describe_cloud_cover(self.cloud_cover)
        dict.__init__(self, cloud_cover=self.cloud_cover, description=self.description)
