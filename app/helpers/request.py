from fastapi import Request
from app.helpers.units import Units


class ExtractUnitsFromRequestState:
    @staticmethod
    def __get_units(arg):
        if arg == Units.IMPERIAL.value:
            return Units.IMPERIAL
        else:
            return Units.METRIC

    def __init__(self, request: Request):
        self.speed_units = ExtractUnitsFromRequestState.__get_units(request.state.units["speed"])
        self.temperature_units = ExtractUnitsFromRequestState.__get_units(request.state.units["temp"])


class ExtractCacheFromRequestState:
    def __init__(self, request: Request):
        self.nocache = request.state.cache["nocache"]
