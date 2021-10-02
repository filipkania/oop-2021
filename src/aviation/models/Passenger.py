from dataclasses import dataclass

from src.aviation.models.Location import Location


@dataclass
class Passenger:
    location: Location
    dead: bool = False
