from app.utils.units import Units
from app.utils.MemcachedCacher import MemcachedCacher, CacheBehaviour
from app.services.OpenWeatherMap.OneCall import OpenWeatherMapOneCall


class CachedOpenWeatherMapOneCall(OpenWeatherMapOneCall):
    def __init__(
        self,
        api_key: str,
        latitude: float,
        longitude: float,
        language: str,
        base_units: Units,
        speed_units: Units,
        temperature_units: Units,
        cache_expires_after: int,
        cache_behaviour: CacheBehaviour,
        cache_key: str,
        memcached_server: str,
    ):
        super().__init__(
            api_key=api_key,
            latitude=latitude,
            longitude=longitude,
            language=language,
            base_units=base_units,
            speed_units=speed_units,
            temperature_units=temperature_units,
        )
        self.cache = MemcachedCacher(
            memcached_server=memcached_server,
            cache_key=cache_key,
            cache_behaviour=cache_behaviour,
            cache_expires_after=cache_expires_after,
        )
        self.response = self.cache.read(self.call)
