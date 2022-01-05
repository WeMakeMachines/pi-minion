from datetime import date
from typing import Optional
from .BaseWeather import BaseWeather, WeatherCondition


class Current(BaseWeather):
    sunrise: date
    sunset: date
    temp: float
    feels_like: float
    rain: Optional[WeatherCondition]
    snow: Optional[WeatherCondition]
