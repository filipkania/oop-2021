from dataclasses import dataclass
from typing import List

from src.aviation.models.Passenger import Passenger
from src.aviation.models.Pilot import Pilot


@dataclass
class Plane:
    passengers: List[Passenger]
    pilot: Pilot

    remaining_fuel: int = 0
    fuel_consumption: int = 25

    destroyed: bool = False

    def boom(self):
        self.destroyed = True
        self.pilot.dead = True
        for passenger in self.passengers:
            passenger.dead = True

    def tank(self, fuel_amount: int):
        self.remaining_fuel += fuel_amount
