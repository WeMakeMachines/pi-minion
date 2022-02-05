from datetime import date
from pydantic import BaseModel
from typing import Optional
from .BaseWeather import BaseWeather


class BaseTemperature(BaseModel):
    day: float
    night: float
    eve: float
    morn: float


class Temperature(BaseTemperature):
    min: float
    max: float


class Day(BaseWeather):
    sunrise: date
    sunset: date
    moonrise: date
    moonset: date
    moon_phase: float
    pop: float
    temp: Temperature
    feels_like: BaseTemperature
    rain: Optional[float]
    snow: Optional[float]
