class Clouds(dict):
    def __init__(self, **kwargs):
        self.cloud_cover = kwargs.get('cloud_cover')
        self.description = self.__describeCloudCover(self.cloud_cover)
        dict.__init__(self, cloud_cover = self.cloud_cover, description = self.description)
        
    def __describeCloudCover(self, cloud_cover):
        description = ["clear", "mostly clear", "mostly clear", "partly cloudy", "partly cloudy", "mostly cloudy", "mostly cloudy", "overcast"]
        
        pick = int((99 if cloud_cover >= 100 else cloud_cover) / (100 / 8))
        
        return description[pick]
