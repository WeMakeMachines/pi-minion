from pydantic import BaseModel
from typing import List

from .Alert import Alert
from .Current import Current
from .Day import Day
from .Hour import Hour


class OneCall(BaseModel):
    lat: float
    lon: float
    timezone: str
    current: Current
    hourly: List[Hour]
    daily: List[Day]
    alerts: List[Alert]
