from .OpenWeatherMap import OpenWeatherMap


class OpenWeatherMapNow(OpenWeatherMap):
    def __init__(
            self,
            api_key,
            base_units,
            speed_units,
            temperature_units,
            latitude,
            longitude
    ):
        url = f"&exclude=minutely,hourly,daily,alerts"

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
        return super().mapper().map_now(self.data["current"])
