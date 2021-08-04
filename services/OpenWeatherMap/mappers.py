from typing import TypedDict

from models.Weather import Clouds, Forecast, Sun
from helpers import Units
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
        self.data = {}

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
                sunset=day["sunset"]
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
        self.data.update({
            "sun": Sun(
                sunrise=now["sunrise"],
                sunset=now["sunset"]
            ),
            "now": self.__map_hour(now)
        })
        return self.data

    def map_hourly(self, hourly):
        self.data.update({
            "hourly": []
        })

        for hour in hourly:
            self.data["hourly"].append(self.__map_hour(hour))

        return self.data

    def map_daily(self, daily):
        self.data.update({
            "daily": []
        })

        for day in daily:
            self.data["daily"].append(self.__map_day(day))

        return self.data
