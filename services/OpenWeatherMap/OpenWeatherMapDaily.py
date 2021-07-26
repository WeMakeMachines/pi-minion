from .OpenWeatherMap import OpenWeatherMap


class OpenWeatherMapDaily(OpenWeatherMap):
    def __init__(
            self,
            api_key,
            base_units,
            speed_units,
            temperature_units,
            latitude,
            longitude
    ):
        url = f"&exclude=current,minutely,hourly,alerts"

        super().__init__(
            api_key,
            base_units,
            speed_units,
            temperature_units,
            latitude,
            longitude,
            url
        )

    def call(self):
        return super().mapper().map_daily(self.data["daily"])
