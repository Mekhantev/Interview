from utils import first


class Vehicle():
    @property
    def size(self):
        return self._size

    def __init__(self, size: int):
        self._size = size


class Car(Vehicle):
    def __init__(self):
        super().__init__(2)


class Motorcycle(Vehicle):
    def __init__(self):
        super().__init__(1)


class ParkingSpot():
    @property
    def empty_space(self):
        return (self.size if self.vehicles is None
                else self.size - sum(v.size for v in self.vehicles))

    def __init__(self, size: int):
        self.size = size
        self.vehicles = []


class Parking():
    def __init__(self):
        self._parking_spots = [
            ParkingSpot(1),
            ParkingSpot(1),
            ParkingSpot(2),
            ParkingSpot(2),
            ParkingSpot(2)
        ]

    def add(self, vehicle: Vehicle):
        try:
            spot = first(spot for spot in self._parking_spots
                         if spot.empty_space >= vehicle.size)
        except ValueError:
            raise Exception('No empty parking spot')
        spot.vehicles.append(vehicle)

    def remove(self, vehicle: Vehicle):
        spot = first(spot for spot in self._parking_spots
                     if vehicle in spot.vehicles)
        spot.vehicles.remove(vehicle)