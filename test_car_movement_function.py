import car_movement_library
import pytest

from random import randint
from typing import Final
from itertools import product, permutations


def test_find_distance_zero_data():
    """Checks the absence of movement at zero speed or zero time
    with other random non-zero data"""

    test_iteration: Final = 10

    for i in range(test_iteration):

        random_data = randint(1, 1000)
        test_weight = randint(1, 10000)

        for permutation in permutations([0, random_data]):

            test_speed, test_time = permutation

            result = car_movement_library.find_distance_traveled(movement_speed=test_speed,
                                                                 time_movement=test_time,
                                                                 car_weight=test_weight)

            assert 'подолав відстань 0 ' in result


def test_find_distance_minus_data():
    """Checks for errors with negative parameters
    and correct value with positive ones"""

    with pytest.raises(ValueError):

        for combination in product([1, -1], repeat=3):

            test_time, test_speed, test_weight = combination

            actual_result = car_movement_library.find_distance_traveled(time_movement=test_time,
                                                                        car_weight=test_weight,
                                                                        movement_speed=test_speed)
            expected = 'Транспортний засіб вагою 1 кг \
рухався 1 секунд зі швидкістю 1 м/сек, \
і подолав відстань 1 метрів'

            assert actual_result == expected


def test_find_distance_valid_data():
    """Checking the correctness of calculations and roundings"""

    test_time = 10.5
    test_speed = 12.275
    test_weight = 5_000

    actual_result = car_movement_library.find_distance_traveled(time_movement=test_time,
                                                                car_weight=test_weight,
                                                                movement_speed=test_speed)
    expected = 'Транспортний засіб вагою 5000 кг \
рухався 10.5 секунд зі швидкістю 12.275 м/сек, \
і подолав відстань 128.89 метрів'

    assert actual_result == expected

