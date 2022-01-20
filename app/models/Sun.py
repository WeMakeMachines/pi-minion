from math import floor


class Sun:
    @staticmethod
    def calc_solar_noon(sunrise: int, sunset: int):
        return round(sunrise + (sunset - sunrise) / 2)

    @staticmethod
    def calc_daylight(sunrise: int, sunset: int):
        seconds_in_hour = 3600
        seconds_in_minute = 60
        duration = sunset - sunrise
        hours = floor(duration / seconds_in_hour)
        minutes = duration % seconds_in_minute

        return {
            "hours": hours,
            "minutes": minutes
        }

    def __init__(self, sunrise: int, sunset: int, uv_index: float):
        self.sunrise = sunrise
        self.sunset = sunset
        self.solar_noon = self.calc_solar_noon(sunrise=sunrise, sunset=sunset)
        self.daylight_length = self.calc_daylight(sunrise=sunrise, sunset=sunset)
        self.uv_index = round(uv_index)
