from multiprocessing import Lock
from pymemcache.client.base import Client

from app.helpers.cache import JsonCacheSerializeDeserialize
from app.services.OpenWeatherMap.GeoCoding import OpenWeatherMapGeoCoding


class CachedOpenWeatherMapGeoCoding(OpenWeatherMapGeoCoding):
    lock = Lock()

    def __init__(
            self,
            api_key: str,
            latitude: float,
            longitude: float,
            language: str,
            memcached_server: str,
            cache_key: str
    ):
        super().__init__(
            api_key,
            latitude,
            longitude,
            language
        )

        self.cache_client: Client = Client(server=memcached_server, serde=JsonCacheSerializeDeserialize(), connect_timeout=10,
                                   timeout=10, no_delay=False)
        self.cache_key: str = f"pinion.weather.open.weather.map.geocoding{cache_key}"
        self.cache_timestamp: int = 0
        self.cached: bool = False
        self.lock.acquire()

        try:
            cache_contents = self.cache_client.get(self.cache_key)

            if cache_contents is not None:
                self.use_cache()
                return

            self.use_request()
            self.write_cache()
        except Exception:
            self.use_cache()
        finally:
            self.lock.release()

    def use_request(self):
        self.raw_response = self.call()

    def use_cache(self):
        cache_contents = self.cache_client.get(self.cache_key)
        self.cached = True
        self.raw_response = cache_contents['cache']

    def write_cache(self):
        self.cache_client.set(key=self.cache_key, value=self.raw_response)
