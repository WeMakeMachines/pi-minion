import hashlib

from enum import Enum, unique


@unique
class CacheExpiresAfter(Enum):
    TODAY = "today"
    DISABLE = "disable"


def hash_string(string: str):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()
