from typing import Union


class Temperature(dict):
    @staticmethod
    def __describe_temperature(temperature):
        description = ["below freezing", "freezing", "very cold", "cold", "moderate", "hot", "very hot", "sweltering"]

        if temperature < 0:
            return description[0]

        if temperature > 30:
            return description[-1]

        pick = int(temperature / 5)

        return description[pick + 1]

    def __init__(self, actual: float, feels_like: Union[float, None]):
        self.actual = actual
        self.feels_like = feels_like

        self.description = self.__describe_temperature(self.actual)
        dict.__init__(self, actual=self.actual, feels_like=self.feels_like, description=self.description)
