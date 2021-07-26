from .OpenWeatherMap import OpenWeatherMap


class OpenWeatherMapHourly(OpenWeatherMap):
    def __init__(
            self,
            api_key,
            base_units,
            speed_units,
            temperature_units,
            latitude,
            longitude
    ):
        url = f"&exclude=current,minutely,daily,alerts"

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
        print(self.data)
        return super().mapper().map_hourly(self.data["hourly"])
