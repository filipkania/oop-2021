from dataclasses import dataclass

from src.aviation.models.Location import Location


@dataclass
class Pilot:
    name: str
    location: Location
    dead: bool = False
    has_license: bool = True
