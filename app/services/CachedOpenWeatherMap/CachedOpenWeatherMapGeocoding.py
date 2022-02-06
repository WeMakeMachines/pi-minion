from app.utils.CacheRequest import CacheRequest, CacheBehaviour
from app.services.OpenWeatherMap.Geocoding import OpenWeatherMapGeocoding


class CachedOpenWeatherMapGeocoding(OpenWeatherMapGeocoding):
    def __init__(
            self,
            api_key: str,
            latitude: float,
            longitude: float,
            language: str,
            cache_behaviour: CacheBehaviour,
            cache_key: str,
            memcached_server: str
    ):
        super().__init__(
            api_key=api_key,
            latitude=latitude,
            longitude=longitude,
            language=language
        )
        self.cache = CacheRequest(
            memcached_server=memcached_server,
            cache_key=cache_key,
            cache_behaviour=cache_behaviour
        )
        self.raw_response = self.cache.read(self.call)
