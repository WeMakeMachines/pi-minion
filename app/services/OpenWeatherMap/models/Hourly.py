from typing import Optional
from .BaseWeather import BaseWeather, WeatherCondition


class Hourly(BaseWeather):
    feels_like: float
    pop: float
    temp: float
    rain: Optional[WeatherCondition]
    snow: Optional[WeatherCondition]
