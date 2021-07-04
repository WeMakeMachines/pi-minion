from config import BaseConfig
from enum import Enum
from flask import request
from functools import wraps
from helpers import elapsed_time_in_minutes
from services import Caching

class Cacheable(Enum):
    TRUE = 1
    FALSE = 2
    DISABLE = 3

def set_caching_properties(cache_expiry_time_in_minutes):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if BaseConfig.DISABLE_CACHING:
                request.cacheable = Cacheable.DISABLE
                
            else:                
                request.cacheable = Cacheable.TRUE
                request.cache = Caching(request.path)
                
                cache = request.cache.read()
                
                if cache != None:
                    elapsed_time = elapsed_time_in_minutes(cache["timestamp"])
                    
                    if elapsed_time < cache_expiry_time_in_minutes:
                        request.cacheable = Cacheable.FALSE
            
            return function(*args, **kwargs)
        return wrapper
    return decorator
