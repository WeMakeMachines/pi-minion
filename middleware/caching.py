from config import BaseConfig
from enum import Enum
from flask import make_response, request
from functools import wraps
from helpers import DateTimeComparison
from services import Caching


class Cacheable(Enum):
    TRUE = 1
    FALSE = 2
    DISABLE = 3


class Valid(Enum):
    THIS_HOUR = 1
    TODAY = 2


def __handle_caching(cache, is_cacheable, api_call):
    data = {}

    if is_cacheable == Cacheable.FALSE:
        cache_contents = cache.read()
        data['cache_timestamp'] = cache_contents['cache_timestamp']
        data['data'] = cache_contents['cache']

    else:
        data['data'] = api_call()

    if is_cacheable == Cacheable.TRUE:
        cache.write(data['data'])

    return data


def __validate_timestamp(timestamp: float, validity_switch):
    date_time_comparison = DateTimeComparison(timestamp)

    if validity_switch == Valid.TODAY:
        return not date_time_comparison.has_day_from_timestamp_passed()

    return not date_time_comparison.has_hour_from_timestamp_passed()


def cache_api_response(valid_for, api_call):
    def decorator(function):
        @wraps(function)
        def wrapper():
            cache = None

            if BaseConfig.DISABLE_CACHING:
                is_cacheable = Cacheable.DISABLE

            else:
                is_cacheable = Cacheable.TRUE
                cache = Caching(request.path)
                cache_contents = cache.read()

                if cache_contents is not None:
                    is_cache_valid = __validate_timestamp(cache_contents["cache_timestamp"], valid_for)

                    if is_cache_valid:
                        is_cacheable = Cacheable.FALSE

            response = make_response(__handle_caching(cache, is_cacheable, api_call))

            return function(response)

        return wrapper

    return decorator
