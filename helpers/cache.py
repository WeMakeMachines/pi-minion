from enum import Enum, unique


@unique
class CacheValidity(Enum):
    HOUR = "hour"
    TODAY = "today"
    DISABLE = "disable"
