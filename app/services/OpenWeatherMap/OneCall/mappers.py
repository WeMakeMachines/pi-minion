from typing import List

from app.models.Alert import Alert
from app.models.Clouds import Clouds
from app.models.Forecast import Forecast
from app.models.Sun import Sun
from app.helpers.units import Units
from .converters import ConvertedTemperature, ConvertedWind
from .models import Hour, Day, Alert as AlertType


class Mapper:
    def __init__(self, base_units: Units, speed_units: Units, temperature_units: Units):
        self.base_units = base_units
        self.speed_units = speed_units
        self.temperature_units = temperature_units

    def __map_hour(self, hour: Hour):
        precipitation_chance = None

        if "pop" in hour:
            precipitation_chance=hour["pop"]

        return {
            "time": hour["dt"],
            "description": Forecast(
                title=hour["weather"][0]["main"],
                body=hour["weather"][0]["description"]
            ),
            "clouds": Clouds(
                cover=hour["clouds"],
                precipitation_chance=precipitation_chance
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

    def __map_day(self, day: Day):
        return {
            "sun": Sun(
                sunrise=day["sunrise"],
                sunset=day["sunset"],
                uv_index=day["uvi"]
            ),
            "description": Forecast(
                title=day["weather"][0]["main"],
                body=day["weather"][0]["description"]
            ),
            "clouds": Clouds(
                cover=day["clouds"],
                precipitation_chance=day["pop"]
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

    def __map_alert(self, alert: AlertType):
        return Alert(
            title=alert["event"],
            issued_by=alert["sender_name"],
            issued_at=alert["start"],
            expires=alert["end"],
            description=alert["description"]
        )

    def map_now(self, now: Hour):
        mapped_hour = self.__map_hour(now)
        mapped_now = {}

        for key in mapped_hour:
            mapped_now[key] = mapped_hour[key]

        mapped_now.update({
            "sun": Sun(
                sunrise=now["sunrise"],
                sunset=now["sunset"],
                uv_index=now["uvi"]
            ),
        })

        return mapped_now

    def map_hourly(self, hourly):
        mapped_hourly = []

        for hour in hourly:
            mapped_hourly.append(self.__map_hour(hour))

        return mapped_hourly

    def map_daily(self, daily: Day):
        mapped_daily = []

        for day in daily:
            mapped_daily.append(self.__map_day(day))

        return mapped_daily

    def map_alerts(self, alerts):
        mapped_alerts = []

        for alert in alerts:
            mapped_alerts.append(self.__map_alert(alert))

        return mapped_alerts
