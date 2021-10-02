from random import randint, getrandbits

from models.Flight import Flight
from models.Location import Location
from models.Passenger import Passenger
from models.Pilot import Pilot
from models.Plane import Plane

if __name__ == "__main__":
    KTW = Location(50.472802, 19.075881)
    LAX = Location(33.942791, -118.410042)

    passengers = [Passenger(location=KTW) for i in range(randint(10, 50))]
    pilot = Pilot("Java Rice", has_license=bool(getrandbits(1)), location=KTW)

    plane = Plane(passengers, pilot)

    distance = KTW.distance_between(LAX)
    amount_to_tank = distance / 100 * (plane.fuel_consumption - getrandbits(1))
    plane.tank(amount_to_tank)

    flight = Flight(origin=KTW, destination=LAX, plane=plane)
    flight.takeoff()
