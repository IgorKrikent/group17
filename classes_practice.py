import time
import requests

from pygame import mixer

sound_beep_url = 'https://zvukitop.com/wp-content/uploads/2020/08/Zvuk-signala-mashyny-klakson-avto-63.mp3'

sound_beep = requests.get(sound_beep_url).content

with open('beep.mp3', mode='wb') as file:

    file.write(sound_beep)


class Car:
    """Template of some car"""

    def __init__(self, *, brand: str,
                 produced_by: str,
                 release_year: int = 2020):

        self.release_year = release_year
        self.brand = brand
        self.produced_by = produced_by
        self.mileage = 0

    def __str__(self):

        result = (f'{self.brand} produced in {self.release_year}, '
                  f'at the {self.produced_by}, with a mileage of {self.mileage} km')

        return result

    @staticmethod
    def beep() -> None:
        """Plays car horn sound when calling"""

        mixer.init()

        mixer.music.load('beep.mp3')

        mixer.music.play(0)
        time.sleep(2)

        return None


class GasolineCar(Car):
    """Gasoline car based on a template of some car,
    takes gasoline consumption in liters per 100 km"""
    def __init__(self, *, brand: str,
                 produced_by: str,
                 fuel_consumption: float,
                 release_year: int = 2020):

        super().__init__(brand=brand, produced_by=produced_by, release_year=release_year)
        self.fuel_consumption = fuel_consumption

    def __str__(self):

        result = super().__str__() + f", with fuel consumption {self.fuel_consumption} liters per 100 km"

        return result


my_car = Car(brand="Kia", produced_by="Kia Corporation")

my_car.mileage += 14_000

other_gasoline_car = GasolineCar(brand="Mersedes",
                                 produced_by="Mersedes-Benz Manufacturing",
                                 fuel_consumption=10.5,
                                 release_year=2015)

my_car.beep()
other_gasoline_car.beep()

print(f"My car is: \n{my_car}")
print(f"My neighbor's car is: \n{other_gasoline_car}")

