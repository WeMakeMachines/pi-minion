from config import BaseConfig
from enum import Enum
from flask import make_response, request
from functools import wraps
from helpers import elapsed_time_in_minutes
from services import Caching


class Cacheable(Enum):
    TRUE = 1
    FALSE = 2
    DISABLE = 3


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


def cache_api_response(cache_expiry_time_in_minutes, api_call):
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
                    elapsed_time = elapsed_time_in_minutes(cache_contents["cache_timestamp"])

                    if elapsed_time < cache_expiry_time_in_minutes:
                        is_cacheable = Cacheable.FALSE

            response = make_response(__handle_caching(cache, is_cacheable, api_call))

            return function(response)

        return wrapper

    return decorator
