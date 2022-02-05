from multiprocessing import Lock
from pymemcache.client.base import Client

from app.helpers.cache import CacheExpiresAfter, JsonCacheSerializeDeserialize
from app.helpers.time import DateTimeComparison
from app.helpers.units import Units
from app.services.OpenWeatherMap.OneCall import OpenWeatherMapOneCall


class CachedOpenWeatherMapOneCall(OpenWeatherMapOneCall):
    lock = Lock()

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
            language: str,
            memcached_server: str,
            cache_key: str,
            cache_expires_after: CacheExpiresAfter,
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

        self.cache_client: Client = Client(server=memcached_server, serde=JsonCacheSerializeDeserialize(), connect_timeout=10,
                                   timeout=10, no_delay=False)
        self.cache_key: str = f"pinion.weather.open.weather.map.one.call{cache_key}"
        self.cache_timestamp: int = 0
        self.cached: bool = False
        self.lock.acquire()

        try:
            if cache_expires_after is CacheExpiresAfter.DISABLE:
                self.use_request()
                return

            cache_contents = self.cache_client.get(self.cache_key)

            if cache_contents is not None:
                is_cache_valid = CachedOpenWeatherMapOneCall.validate_cache_timestamp(
                    timestamp=cache_contents["cache_timestamp"],
                    cache_expires_after=cache_expires_after
                )

                if is_cache_valid:
                    self.use_cache()
                    return

            self.use_request()
            self.write_cache()
        except Exception:
            self.use_cache()
        finally:
            self.lock.release()

    def use_request(self):
        self.raw_response.update(self.call())

    def use_cache(self):
        cache_contents = self.cache_client.get(self.cache_key)
        self.cached = True
        self.cache_timestamp = cache_contents['cache_timestamp']
        self.raw_response.update(cache_contents['cache'])

    def write_cache(self):
        self.cache_client.set(key=self.cache_key, value=self.raw_response, expire=60*60*24*14)
