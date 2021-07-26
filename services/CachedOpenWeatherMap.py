from .OpenWeatherMap import OpenWeatherMap
from .FileCache import FileCache
from config import BaseConfig
from helpers import Cacheable, CacheValidity, DateTimeComparison


class CachedOpenWeatherMap(OpenWeatherMap):
    @staticmethod
    def validate_timestamp(timestamp: float, validity: CacheValidity):
        date_time_comparison = DateTimeComparison(timestamp)

        if validity is CacheValidity.TODAY:
            return not date_time_comparison.has_day_from_timestamp_passed()

        return not date_time_comparison.has_hour_from_timestamp_passed()

    def __init__(
            self,
            api_key,
            base_units,
            speed_units,
            temperature_units,
            latitude,
            longitude
    ):
        super().__init__(
            api_key,
            base_units,
            speed_units,
            temperature_units,
            latitude,
            longitude
        )

        self.cache = None
        self.is_cacheable = Cacheable.DISABLE

        if BaseConfig.CACHE_VALIDITY is not CacheValidity.DISABLE:
            self.is_cacheable = Cacheable.TRUE
            self.cache = FileCache('open_weather_map')
            cache_contents = self.cache.read()

            if cache_contents is not None:
                is_cache_valid = CachedOpenWeatherMap.validate_timestamp(
                    timestamp=cache_contents["cache_timestamp"],
                    validity=BaseConfig.CACHE_VALIDITY
                )

                if is_cache_valid:
                    self.is_cacheable = Cacheable.FALSE

        self.handle_caching()

    def handle_caching(self):
        if self.is_cacheable is Cacheable.FALSE:
            cache_contents = self.cache.read()
            self.parsed_data['cache_timestamp'] = cache_contents['cache_timestamp']
            self.raw_response.update(cache_contents['cache'])

        else:
            self.raw_response.update(self.call())

        if self.is_cacheable is Cacheable.TRUE:
            self.cache.write(self.raw_response)
