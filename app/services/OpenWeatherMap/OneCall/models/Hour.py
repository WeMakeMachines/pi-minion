from typing import Optional
from .BaseWeather import BaseWeather, WeatherCondition


class Hour(BaseWeather):
    feels_like: float
    pop: float
    temp: float
    rain: Optional[WeatherCondition]
    snow: Optional[WeatherCondition]
