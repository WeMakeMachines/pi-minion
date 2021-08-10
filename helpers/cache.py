from enum import Enum, unique


@unique
class CacheExpiresAfter(Enum):
    TODAY = "today"
    DISABLE = "disable"
