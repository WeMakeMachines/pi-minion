from models.Weather import Clouds, Forecast, Sun, Temperature
from helpers import Units
from .normalised import NormalisedWind


class Mapper:
    def __init__(self, units: Units):
        self.units = units
        self.data = {
            "units": units.value
        }

    def __map_hour(self, hour):
        return {
            "time": hour["dt"],
            "description": Forecast(
                main=hour["weather"][0]["main"],
                description=hour["weather"][0]["description"]
            ),
            "clouds": Clouds(
                cloud_cover=hour["clouds"]
            ),
            "temperature": Temperature(
                units=self.units,
                actual=hour["temp"],
                feels_like=hour["feels_like"]
            ),
            "wind": NormalisedWind(
                units=self.units,
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
                description=day["weather"][0]["description"]
            ),
            "clouds": Clouds(
                cloud_cover=day["clouds"]
            ),
            "temperature": {
                "morning": Temperature(
                    units=self.units,
                    actual=day["temp"]["morn"],
                    feels_like=day["feels_like"]["morn"]
                ),
                "day": Temperature(
                    units=self.units,
                    actual=day["temp"]["day"],
                    feels_like=day["feels_like"]["day"]
                ),
                "evening": Temperature(
                    units=self.units,
                    actual=day["temp"]["eve"],
                    feels_like=day["feels_like"]["eve"]
                ),
                "night": Temperature(
                    units=self.units,
                    actual=day["temp"]["night"],
                    feels_like=day["feels_like"]["night"]
                ),
                "max": Temperature(
                    units=self.units,
                    actual=day["temp"]["max"]
                ),
                "min": Temperature(
                    units=self.units,
                    actual=day["temp"]["min"]
                )
            },
            "wind": NormalisedWind(
                units=self.units,
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
        data = []

        for hour in hourly:
            data.append(self.__map_hour(hour))

        self.data.update({
            "hourly": data
        })
        return self.data

    def map_daily(self, daily):
        data = []

        for day in daily:
            data.append(self.__map_day(day))

        self.data.update({
            "daily": data
        })
        return self.data
