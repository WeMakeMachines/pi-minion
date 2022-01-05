from datetime import date
from pydantic import BaseModel
from typing import List


class Alert(BaseModel):
    sender_name: str
    event: str
    start: date
    end: date
    description: str
    tags: List[str]
