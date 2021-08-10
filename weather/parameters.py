from helpers import Units


class ExtractWeatherParamsFromRequest:
    @staticmethod
    def __get_units(arg):
        if arg == Units.IMPERIAL.value:
            return Units.IMPERIAL
        else:
            return Units.METRIC

    def __init__(self, request):
        self.speed_units = ExtractWeatherParamsFromRequest.__get_units(request.args.get("speed"))
        self.temperature_units = ExtractWeatherParamsFromRequest.__get_units(request.args.get("temp"))
        self.latitude = request.args.get("lat")
        self.longitude = request.args.get("long")


class ExtractCacheParamsFromRequest:
    def __init__(self, request):
        self.nocache = request.args.get("nocache")
