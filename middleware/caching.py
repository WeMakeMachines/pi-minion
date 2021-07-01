from config import BaseConfig
from flask import request
from functools import wraps
from helpers import elapsed_time_in_minutes
from services import Caching

def caching(cache_expiry_time_in_minutes):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            request.cacheable = True            
            request.cache = Caching(request.path)
            
            cache = request.cache.read()
            
            if not cache == None:
                elapsed_time = elapsed_time_in_minutes(cache["timestamp"])
                
                if elapsed_time < cache_expiry_time_in_minutes:
                    request.cacheable = False
            
            return function(*args, **kwargs)
        return wrapper
    return decorator
