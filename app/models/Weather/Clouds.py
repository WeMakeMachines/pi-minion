from typing import Optional


class Clouds:
    def __init__(self, cover: int, precipitation_chance: Optional[float]):
        self.cover = cover
        if precipitation_chance is not None:
            self.precipitation_chance = precipitation_chance
