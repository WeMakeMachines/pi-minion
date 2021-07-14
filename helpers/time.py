from datetime import datetime


class DateTimeComparison:
    def __init__(self, timestamp: float):
        self.datetime = datetime.fromtimestamp(timestamp)
        self.now = datetime.now()

    def has_hour_from_timestamp_passed(self):

        if self.now.hour > self.datetime.hour:
            return True

        return False

    def has_day_from_timestamp_passed(self):

        if self.now.day > self.datetime.day:
            return True

        return False
