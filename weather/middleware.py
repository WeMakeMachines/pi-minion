from config import BaseConfig
from flask import request
from werkzeug.datastructures import OrderedMultiDict


# organise the client params into a specific order
def normalise_weather_params(function):
    def decorator():
        units_params = {
            "speed": BaseConfig.BASE_UNITS.value,
            "temp": BaseConfig.BASE_UNITS.value
        }
        location_params = {
            "lat": BaseConfig.LATITUDE,
            "long": BaseConfig.LONGITUDE
        }
        ordered_params = {}

        for param in units_params:
            client_value = request.args.get(param)

            if client_value is not None:
                ordered_params[param] = client_value
            else:
                ordered_params[param] = units_params[param]

        for param in location_params:
            client_value = request.args.get(param)
            if client_value is not None:
                ordered_params[param] = client_value
            else:
                ordered_params[param] = location_params[param]

        request.parameter_storage_class = OrderedMultiDict
        request.args = ordered_params

        return function()

    return decorator
