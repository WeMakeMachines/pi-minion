class Temperature(dict):
    def __init__(self, **kwargs):
        self.actual = kwargs.get('actual')
        self.feels_like = kwargs.get('feels_like')
        
        self.description = self.__describeTemperature(self.actual)
        dict.__init__(self, actual = self.actual, feels_like = self.feels_like, description = self.description)
        
    def __describeTemperature(self, temperature):
        description = ["below freezing", "freezing", "very cold", "cold", "moderate", "hot", "very hot", "sweltering"]
        
        if temperature < 0:
            return description[0]
        
        if temperature > 30:
            return description[-1]
        
        pick = int(temperature / 5)
        
        return description[pick + 1]
