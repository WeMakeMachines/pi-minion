from datetime import datetime


class DateTimeComparison:
    def __init__(self, timestamp: float):
        self.datetime = datetime.fromtimestamp(timestamp)
        self.now = datetime.now()

    def get_diff_in_minutes(self):
        diff = (self.now - self.datetime)
        diff_in_minutes = diff.total_seconds() / 60

        return diff_in_minutes

    def has_hour_from_timestamp_passed(self):
        diff_in_minutes = self.get_diff_in_minutes()

        if diff_in_minutes > 60:
            return True

        return False

    def has_day_from_timestamp_passed(self):
        diff_in_minutes = self.get_diff_in_minutes()
        diff_in_hours = diff_in_minutes / 60

        if diff_in_hours > 24:
            return True

        return False
