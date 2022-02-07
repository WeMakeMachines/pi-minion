from multiprocessing import Lock
from pymemcache.client.base import Client
from typing import Callable

from .CacheValidation import CacheValidation
from .serde import JsonCacheSerializeDeserialize
from .types import CacheBehaviour


class CacheRequest:
    def __init__(
        self,
        memcached_server: str,
        cache_key: str,
        cache_behaviour: CacheBehaviour = CacheBehaviour.CACHE_ONCE,
        cache_expires_after: int = 0,
    ):
        self.cache_client: Client = Client(
            server=memcached_server,
            serde=JsonCacheSerializeDeserialize(),
            connect_timeout=10,
            timeout=10,
            no_delay=False,
        )
        self.cache_key = cache_key
        self.cache_behaviour = cache_behaviour
        self.cache_expires_after = cache_expires_after
        self.cache_timestamp: int = 0
        self.cached: bool = False

    def read(self, request: Callable):
        try:
            cache_contents = self.__read_cache()

            if self.cache_behaviour is CacheBehaviour.DISABLE:
                return request()

            if cache_contents is not None:
                if self.cache_expires_after > 0:
                    is_cache_valid = CacheValidation.validate_cache_timestamp(
                        timestamp=cache_contents["cache_timestamp"],
                        cache_expires_after=self.cache_expires_after,
                    )

                    if is_cache_valid:
                        return self.__use_cache(cache_contents)

                if self.cache_behaviour is CacheBehaviour.CACHE_ONCE:
                    return self.__use_cache(cache_contents)

                if self.cache_behaviour is CacheBehaviour.RENEW_DAILY:
                    is_cache_valid = CacheValidation.validate_cache_timestamp_is_today(
                        timestamp=cache_contents["cache_timestamp"]
                    )

                    if is_cache_valid:
                        return self.__use_cache(cache_contents)

            response = request()
            self.__write_to_cache(response)
            return response

        except Exception:
            return request()

    def __read_cache(self):
        return self.cache_client.get(self.cache_key)

    def __use_cache(self, cache_contents):
        self.cache_timestamp = cache_contents["cache_timestamp"]
        self.cached = True
        return cache_contents["cache"]

    def __write_to_cache(self, response):
        lock = Lock()
        lock.acquire()
        self.cache_client.set(
            key=self.cache_key, value=response, expire=60 * 60 * 24 * 14
        )
        lock.release()
