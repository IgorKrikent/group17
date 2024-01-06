from abc import ABC, abstractmethod

import math


class Transport(ABC):
    """Abstract transport,
    takes brand, max speed of transport (in kilometers per hour)
    and position (coordinates: x at first, y - at second)"""

    def __init__(self, *, brand: str, max_speed: float, position: tuple):

        self.brand = brand
        self.max_speed = max_speed
        self.position = dict.fromkeys(["X", "Y"])
        self.position["X"], self.position["Y"] = position

    @abstractmethod
    def move(self, *, angle: float, distance: float) -> None:
        """Change position of the something motile,
        takes angle in degrees, distance in kilometers"""

        angle_radians = angle * (3.14 / 180)

        self.position["X"] += math.cos(angle_radians) * distance
        self.position["Y"] += math.sin(angle_radians) * distance

        return None


class GasolineTransport(Transport):
    """Gasoline transport based on abstract transport,
    takes volume of the tank in liters
    and fuel consumption in liters per 100 kilometers"""

    def __init__(self, *, brand: str,
                 max_speed: float,
                 position: tuple,
                 gasoline_tank_volume: float,
                 fuel_consumption: float):

        super().__init__(brand=brand, max_speed=max_speed, position=position)

        self.fuel_consumption = fuel_consumption
        self.gasoline_tank_volume = gasoline_tank_volume

        self.remaining_fuel = gasoline_tank_volume

        self.mileage = 0

    def remaining_fuel(self) -> float:
        """Property 'remaining_fuel', method - get"""

        return self._remaining_fuel

    def remaining_fuel_set(self, value: float) -> None:
        """Property 'remaining_fuel', method - set,
        raise 'ValueError' if remaining fuel less than zero
        or more than tank volume"""

        if 0 <= value <= self.gasoline_tank_volume:

            self._remaining_fuel = value

        else:

            raise ValueError

    remaining_fuel = property(remaining_fuel, remaining_fuel_set)

    def mileage(self):
        """Property 'mileage', method - get"""

        return self._mileage

    def mileage_set(self, value: float):
        """Property 'mileage', method - set,
        raise 'ValueError' if mileage less than zero"""

        if value >= 0:

            self._mileage = value

        else:

            raise ValueError

    mileage = property(mileage, mileage_set)

    def move(self, *, angle: float, distance: float) -> None:
        """Reduces the amount of fuel and changes the mileage
         according to the distance traveled;
         triggers the 'move' function defined in the super class"""

        gasoline_need = distance * self.fuel_consumption / 100

        if self.remaining_fuel >= gasoline_need:

            super().move(angle=angle, distance=distance)

            self.remaining_fuel -= distance * self.fuel_consumption / 100

            self.mileage += distance

        else:

            print(f"{self}, can't move {distance} km due to lack of fuel")

        return None

    def refuelling(self, fuel_volume: float) -> None:
        """Refills the own tank with the specified number of liters of fuel"""

        if fuel_volume < 0:

            raise ValueError

        try:

            self.remaining_fuel += fuel_volume

        except ValueError:

            print(f"\nWARNING, OPERATION LOST:"
                  f" \nIt is impossible to fill {fuel_volume} liters of fuel,"
                  f" \nthere is not enough space in the {self}!!!\n")

        return None

    def fuel_overflow(self, other, fuel_volume: float) -> None:
        """Transfers fuel from one vehicle to another,
        both vehicles must belong to the 'GasolineTransport' class,
        takes the volume of fuel for transfer (in liters)"""

        if fuel_volume < 0:

            raise ValueError

        try:

            self.remaining_fuel -= fuel_volume

            other.remaining_fuel += fuel_volume

        except ValueError:

            print(f"\nWARNING, OPERATION LOST:"
                  f" \n{self} cannot transfer {fuel_volume} liters of fuel to a {other}."
                  f" \nThere is not enough fuel or the other's tank will not fit as much!!!\n")

        return None

