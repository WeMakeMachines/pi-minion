import datetime

from flask import request
from functools import wraps
from services import Caching
from helpers import elapsed_time_in_minutes

def caching(function):
    @wraps(function)
    def __caching(*args, **kwargs):
        request.cache = Caching(request.path)
        request.cacheable = True
        
        cache = request.cache.read()
        
        if not cache == None:
            elapsed_time = elapsed_time_in_minutes(cache['timestamp'])
            
            if elapsed_time < request.threshold:
                request.cacheable = False
        
        return function(*args, **kwargs)
    return __caching

def caching_60_minutes(function):
    @wraps(function)
    def __caching(*args, **kwargs):
        request.threshold = 60
        
        return function(*args, **kwargs)
    return __caching

def caching_24_hours(function):
    @wraps(function)
    def __caching(*args, **kwargs):
        request.threshold = 60 * 24
        
        return function(*args, **kwargs)
    return __caching
