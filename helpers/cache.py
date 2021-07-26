from enum import Enum, unique


@unique
class Cacheable(Enum):
    TRUE = 1
    FALSE = 2
    DISABLE = 3


@unique
class CacheValidity(Enum):
    HOUR = "hour"
    TODAY = "today"
    DISABLE = "disable"
