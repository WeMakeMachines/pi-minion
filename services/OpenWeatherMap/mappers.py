from models.Weather import Clouds, Forecast, Sun, Temperature
from helpers import Units
from .normalised import NormalisedWind


def map_now(now, units: Units):
    return {
        "sun": Sun(
            sunrise=now["sunrise"],
            sunset=now["sunset"]
        ),
        "now": map_hourly(now, units)
    }


def map_hourly(hourly, units: Units):
    return {
        "time": hourly["dt"],
        "description": Forecast(
            main=hourly["weather"][0]["main"],
            description=hourly["weather"][0]["description"]
        ),
        "clouds": Clouds(
            cloud_cover=hourly["clouds"]
        ),
        "temperature": Temperature(
            units=units,
            actual=hourly["temp"],
            feels_like=hourly["feels_like"]
        ),
        "wind": NormalisedWind(
            units=units,
            speed=hourly["wind_speed"],
            degrees=hourly["wind_deg"]
        )
    }


def map_daily(daily, units: Units):
    return {
        "sun": Sun(
            sunrise=daily["sunrise"],
            sunset=daily["sunset"]
        ),
        "description": Forecast(
            main=daily["weather"][0]["main"],
            description=daily["weather"][0]["description"]
        ),
        "clouds": Clouds(
            cloud_cover=daily["clouds"]
        ),
        "temperature": {
            "morning": Temperature(
                units=units,
                actual=daily["temp"]["morn"],
                feels_like=daily["feels_like"]["morn"]
            ),
            "day": Temperature(
                units=units,
                actual=daily["temp"]["day"],
                feels_like=daily["feels_like"]["day"]
            ),
            "evening": Temperature(
                units=units,
                actual=daily["temp"]["eve"],
                feels_like=daily["feels_like"]["eve"]
            ),
            "night": Temperature(
                units=units,
                actual=daily["temp"]["night"],
                feels_like=daily["feels_like"]["night"]
            ),
            "max": Temperature(
                units=units,
                actual=daily["temp"]["max"]
            ),
            "min": Temperature(
                units=units,
                actual=daily["temp"]["min"]
            )
        },
        "wind": NormalisedWind(
            units=units,
            speed=daily["wind_speed"],
            degrees=daily["wind_deg"],
            gust=daily["wind_gust"]
        )
    }
