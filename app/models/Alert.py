from datetime import date


class Alert:
    def __init__(
        self,
        title: str,
        issued_by: str,
        issued_at: date,
        expires: date,
        description: str,
    ):
        self.title = title.capitalize()
        self.issued_by = issued_by.capitalize()
        self.issued_at = issued_at
        self.expires = expires
        self.description = description.capitalize()
