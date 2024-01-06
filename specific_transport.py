from abstract_transport import GasolineTransport


class GasolineCar(GasolineTransport):
    """Gasoline car class, based on 'GasolineTransport',
    have pillows availability and passengers capacity fields"""

    def __init__(self, *, brand: str,
                 max_speed: float,
                 position: tuple,
                 gasoline_tank_volume: float,
                 fuel_consumption: float,
                 pillows_availability: bool,
                 passengers_capacity: int = 4):

        super().__init__(brand=brand,
                         max_speed=max_speed,
                         position=position,
                         gasoline_tank_volume=gasoline_tank_volume,
                         fuel_consumption=fuel_consumption)

        self.pillows_availability = pillows_availability
        self.passengers_capacity = passengers_capacity

    def __str__(self):

        return (f'{self.brand} car'
                f' with a tank capacity of {self.gasoline_tank_volume} liters')


class GasolineBike(GasolineTransport):
    """Gasoline bike class, based on 'GasolineTransport',
    have cradle availability field"""

    def __init__(self, *, brand: str,
                 max_speed: float,
                 position: tuple,
                 gasoline_tank_volume: float,
                 fuel_consumption: float,
                 cradle_availability: bool):

        super().__init__(brand=brand,
                         max_speed=max_speed,
                         position=position,
                         gasoline_tank_volume=gasoline_tank_volume,
                         fuel_consumption=fuel_consumption)

        self.cradle_availability = cradle_availability

    def __str__(self):

        return (f'{self.brand} motorcycle'
                f' with a tank capacity of {self.gasoline_tank_volume} liters')


my_car = GasolineCar(brand="audi",
                     max_speed=300,
                     position=(0, 0),
                     gasoline_tank_volume=60,
                     fuel_consumption=7,
                     pillows_availability=True)

my_neighbour_bike = GasolineBike(brand="Honda",
                                 max_speed=160,
                                 position=(0, 5),
                                 gasoline_tank_volume=35,
                                 fuel_consumption=6,
                                 cradle_availability=False)

my_car.move(angle=45, distance=300)

my_neighbour_bike.move(angle=30, distance=450)

my_car.refuelling(20)

my_car.fuel_overflow(my_neighbour_bike, 100)

print(f'{my_car.remaining_fuel=}, {my_car.mileage=}')
print(f'{my_neighbour_bike.remaining_fuel=}, {my_neighbour_bike.mileage=}')

