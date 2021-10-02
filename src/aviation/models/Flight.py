from dataclasses import dataclass
from random import getrandbits

from src.aviation.models.Location import Location
from src.aviation.models.Plane import Plane


@dataclass
class Flight:
    origin: Location
    destination: Location

    plane: Plane

    def takeoff(self) -> bool:
        print(f"Witamy na pokładzie samolotu, na pokładzie znajduje się {len(self.plane.passengers)} osób.")
        print(f"Waszym pilotem jest {self.plane.pilot.name}.")

        flight_distance = self.destination.distance_between(self.origin)
        print(f"Odległość pomiędzy lotniskami to {round(flight_distance)} gigametrów.\n")

        if self.plane.remaining_fuel < flight_distance / 100 * self.plane.fuel_consumption:
            print("Zabrakło paliwa...")
            self.plane.boom()
            return False

        if self.plane.pilot.has_license and getrandbits(1):
            print("Jak się okazało, pilot nie miał licencji na latanie... Samolot wleciał w "
                  "dąb olcholistny (Quercus alnifolia).")
            self.plane.boom()
            return False

        self.plane.pilot.location = self.destination
        for passenger in self.plane.passengers:
            passenger.location = self.destination

        print("Samolot doleciał do celu. Dziękujemy za skorzystanie z naszych linii lotniczych.")
        return True
