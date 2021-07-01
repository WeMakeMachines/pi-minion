import datetime;
import math

def elapsed_time_in_minutes(timestamp: float):
    secondsInMinutes = 60
    timeNow = datetime.datetime.now().timestamp()
    
    return (math.floor(timeNow) - math.floor(timestamp)) / secondsInMinutes
