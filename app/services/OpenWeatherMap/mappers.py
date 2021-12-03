from typing import TypedDict

from app.models.Weather.Clouds import Clouds
from app.models.Weather.Forecast import Forecast
from app.models.Weather.Sun import Sun
from app.helpers.units import Units
from .converters import ConvertedTemperature, ConvertedWind


class MapperUnits(TypedDict):
    base_units: Units
    speed_units: Units
    temperature_units: Units


class Mapper:
    def __init__(self, units: MapperUnits):
        self.base_units = units["base_units"]
        self.speed_units = units["speed_units"]
        self.temperature_units = units["temperature_units"]

    def __map_hour(self, hour):
        return {
            "time": hour["dt"],
            "description": Forecast(
                main=hour["weather"][0]["main"],
                text=hour["weather"][0]["description"]
            ),
            "clouds": Clouds(
                cover=hour["clouds"]
            ),
            "temperature": ConvertedTemperature(
                base_units=self.base_units,
                units=self.temperature_units,
                actual=hour["temp"],
                feels_like=hour["feels_like"]
            ),
            "wind": ConvertedWind(
                base_units=self.base_units,
                units=self.speed_units,
                speed=hour["wind_speed"],
                degrees=hour["wind_deg"]
            )
        }

    def __map_day(self, day):
        return {
            "sun": Sun(
                sunrise=day["sunrise"],
                sunset=day["sunset"],
                uv=day["uvi"]
            ),
            "description": Forecast(
                main=day["weather"][0]["main"],
                text=day["weather"][0]["description"]
            ),
            "clouds": Clouds(
                cover=day["clouds"]
            ),
            "temperature": {
                "morning": ConvertedTemperature(
                    base_units=self.base_units,
                    units=self.temperature_units,
                    actual=day["temp"]["morn"],
                    feels_like=day["feels_like"]["morn"]
                ),
                "day": ConvertedTemperature(
                    base_units=self.base_units,
                    units=self.temperature_units,
                    actual=day["temp"]["day"],
                    feels_like=day["feels_like"]["day"]
                ),
                "evening": ConvertedTemperature(
                    base_units=self.base_units,
                    units=self.temperature_units,
                    actual=day["temp"]["eve"],
                    feels_like=day["feels_like"]["eve"]
                ),
                "night": ConvertedTemperature(
                    base_units=self.base_units,
                    units=self.temperature_units,
                    actual=day["temp"]["night"],
                    feels_like=day["feels_like"]["night"]
                ),
                "max": ConvertedTemperature(
                    base_units=self.base_units,
                    units=self.temperature_units,
                    actual=day["temp"]["max"]
                ),
                "min": ConvertedTemperature(
                    base_units=self.base_units,
                    units=self.temperature_units,
                    actual=day["temp"]["min"]
                )
            },
            "wind": ConvertedWind(
                base_units=self.base_units,
                units=self.speed_units,
                speed=day["wind_speed"],
                degrees=day["wind_deg"],
                gust=day["wind_gust"]
            )
        }

    def map_now(self, now):
        mapped_hour = self.__map_hour(now)
        mapped_now = {}

        for key in mapped_hour:
            mapped_now[key] = mapped_hour[key]

        mapped_now.update({
            "sun": Sun(
                sunrise=now["sunrise"],
                sunset=now["sunset"],
                uv=now["uvi"]
            ),
        })

        return mapped_now

    def map_hourly(self, hourly):
        mapped_hourly = []

        for hour in hourly:
            mapped_hourly.append(self.__map_hour(hour))

        return mapped_hourly

    def map_daily(self, daily):
        mapped_daily = []

        for day in daily:
            mapped_daily.append(self.__map_day(day))

        return mapped_daily
