from app.utils.time import DateTimeComparison


class CacheValidation:
    @staticmethod
    def validate_cache_timestamp(timestamp: float, cache_expires_after: int) -> bool:
        date_time_comparison = DateTimeComparison(timestamp)

        return not date_time_comparison.has_time_from_timestamp_passed(cache_expires_after)

    @staticmethod
    def validate_cache_timestamp_is_today(timestamp: float) -> bool:
        date_time_comparison = DateTimeComparison(timestamp)

        return not date_time_comparison.has_day_from_timestamp_passed()
