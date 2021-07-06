import requests
import json

from models.Weather import Clouds, Sun, Temperature, Wind


# Interfaces with the OpenWeatherMap API
# Docs: https://openweathermap.org/api/one-call-api
class OpenWeatherMap:
    @staticmethod
    def __parse_hourly_object(hourly):
        return {
            "time": hourly["dt"],
            "description": hourly["weather"][0]["description"],
            "clouds": Clouds(
                cloud_cover=hourly["clouds"]
            ),
            "temperature": Temperature(
                actual=hourly["temp"],
                feels_like=hourly["feels_like"]
            ),
            "wind": Wind(
                speed=hourly["wind_speed"],
                degrees=hourly["wind_deg"]
            )
        }

    @staticmethod
    def __parse_daily_object(daily):
        return {
            "sun": Sun(
                sunrise=daily["sunrise"],
                sunset=daily["sunset"]
            ),
            "wind": Wind(
                speed=daily["wind_speed"],
                degrees=daily["wind_deg"],
                gust=daily["wind_gust"]
            ),
            "temperature": {
                "morning": Temperature(
                    actual=daily["temp"]["morn"],
                    feels_like=daily["feels_like"]["morn"]
                ),
                "day": Temperature(
                    actual=daily["temp"]["day"],
                    feels_like=daily["feels_like"]["day"]
                ),
                "evening": Temperature(
                    actual=daily["temp"]["eve"],
                    feels_like=daily["feels_like"]["eve"]
                ),
                "night": Temperature(
                    actual=daily["temp"]["night"],
                    feels_like=daily["feels_like"]["night"]
                ),
                "max": Temperature(
                    actual=daily["temp"]["max"]
                ),
                "min": Temperature(
                    actual=daily["temp"]["min"]
                )
            }
        }

    def __init__(self, api_key: str, latitude: float, longitude: float, units: str = "metric"):
        self.api_key = api_key
        self.latitude = latitude
        self.longitude = longitude
        self.units = units

    def now(self):
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/onecall?lat={self.latitude}&lon={self.longitude}&appid={self.api_key}&units={self.units}&exclude=minutely,hourly,daily,alerts")

        data = json.loads(response.text)
        now = data["current"]

        return {
            "sun": Sun(
                sunrise=now["sunrise"],
                sunset=now["sunset"]
            ),
            "now": self.__parse_hourly_object(now)
        }

    def hourly(self):
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/onecall?lat={self.latitude}&lon={self.longitude}&appid={self.api_key}&units={self.units}&exclude=current,minutely,daily,alerts")

        data = json.loads(response.text)

        hourly = []

        for item in data["hourly"]:
            hourly.append(self.__parse_hourly_object(item))

        return hourly

    def daily(self):
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/onecall?lat={self.latitude}&lon={self.longitude}&appid={self.api_key}&units={self.units}&exclude=current,minutely,hourly,alerts")

        data = json.loads(response.text)

        daily = []

        for day in data["daily"]:
            daily.append(self.__parse_daily_object(day))

        return daily