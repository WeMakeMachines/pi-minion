from helpers import CacheExpiresAfter, DateTimeComparison, Units
from API import OpenWeatherMap
from .FileCache import FileCache


class CachedOpenWeatherMap(OpenWeatherMap):
    @staticmethod
    def validate_cache_timestamp(timestamp: float, cache_expires_after: CacheExpiresAfter or int) -> bool:
        date_time_comparison = DateTimeComparison(timestamp)

        if cache_expires_after is CacheExpiresAfter.TODAY:
            return not date_time_comparison.has_day_from_timestamp_passed()

        if isinstance(cache_expires_after, int):
            return not date_time_comparison.has_time_from_timestamp_passed(cache_expires_after)

        return False

    def __init__(
            self,
            api_key: str,
            base_units: Units,
            speed_units: Units,
            temperature_units: Units,
            latitude: float,
            longitude: float,
            cache_key: str,
            cache_expires_after: CacheExpiresAfter,
            language: str
    ):
        super().__init__(
            api_key,
            base_units,
            speed_units,
            temperature_units,
            latitude,
            longitude,
            language
        )

        self.cache = None

        if cache_expires_after is CacheExpiresAfter.DISABLE:
            self.use_request()
            return

        self.cache = FileCache(cache_key)
        cache_contents = self.cache.read()

        if cache_contents is not None:
            is_cache_valid = CachedOpenWeatherMap.validate_cache_timestamp(
                timestamp=cache_contents["cache_timestamp"],
                cache_expires_after=cache_expires_after
            )

            if is_cache_valid:
                self.use_cache()
                return

        self.use_request()
        self.write_cache()

    def use_request(self):
        self.raw_response.update(self.call())

    def use_cache(self):
        cache_contents = self.cache.read()
        self.parsed_data['cache_timestamp'] = cache_contents['cache_timestamp']
        self.raw_response.update(cache_contents['cache'])

    def write_cache(self):
        self.cache.write(self.raw_response)
