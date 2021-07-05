import datetime
import math


def elapsed_time_in_minutes(timestamp: float):
    seconds_in_minutes = 60
    time_now = datetime.datetime.now().timestamp()

    return (math.floor(time_now) - math.floor(timestamp)) / seconds_in_minutes
