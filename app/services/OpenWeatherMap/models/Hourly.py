from typing import Optional
from .BaseWeather import BaseWeather, WeatherCondition


class Hourly(BaseWeather):
    temp: float
    feels_like: float
    rain: Optional[WeatherCondition]
    snow: Optional[WeatherCondition]
