import datetime

from helpers import hash_string


class MemoryCache:
    cache = {}

    def read(self, key: str):
        cache_key = hash_string(key)
        cache = self.cache.get(cache_key)

        return cache

    def write(self, key: str, data):
        cache_key = hash_string(key)
        timestamp = datetime.datetime.now().timestamp()

        self.cache[cache_key] = {
            "cache_timestamp": timestamp,
            "cache": data
        }
