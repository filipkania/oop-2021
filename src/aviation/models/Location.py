from dataclasses import dataclass


@dataclass
class Location:
    latitude: float
    longitude: float

    # https://www.python.org/dev/peps/pep-0484/#forward-references
    def distance_between(self, destination: 'Location') -> (int, int):
        latitude_delta = max(self.latitude, destination.latitude) - min(self.latitude, destination.latitude)
        longitude_delta = max(self.longitude, destination.longitude) - min(self.longitude, destination.longitude)

        return latitude_delta + longitude_delta
