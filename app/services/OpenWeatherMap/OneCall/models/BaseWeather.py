from datetime import date
from pydantic import BaseModel
from typing import List, Optional


class WeatherCondition(BaseModel):
    hour: float

    class Config:
        fields = {"hour": "1h"}


class WeatherDescription(BaseModel):
    id: int
    main: str
    description: str
    icon: str


class BaseWeather(BaseModel):
    clouds: int
    dew_point: float
    dt: date
    humidity: int
    pressure: int
    uvi: float
    wind_deg: int
    wind_speed: float
    weather: List[WeatherDescription]
    wind_gust: Optional[float]
