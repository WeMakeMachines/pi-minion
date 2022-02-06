from enum import Enum, unique


@unique
class CacheBehaviour(Enum):
    RENEW_DAILY = "renew_daily"
    CACHE_ONCE = "cache_once"
    USER_SPECIFIED = "user_specified"
    DISABLE = "disable"
