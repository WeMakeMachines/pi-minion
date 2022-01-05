from pydantic import BaseModel
from typing import Optional


class Clouds(BaseModel):
    cover: int
    precipitation_chance: Optional[float]
