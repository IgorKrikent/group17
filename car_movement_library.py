def find_distance_traveled(*, time_movement: int | float,
                           movement_speed: int | float,
                           car_weight: int | float) -> str:
    """Takes time (in seconds), speed (meters per second) and car weight (kg).
    Finds the distance covered by the car and returns a text message
    with the parameters of the movement and the weight of the car"""

    distance = time_movement * movement_speed

    result_message = f'Транспортний засіб вагою {car_weight} кг \
рухався {time_movement} секунд зі швидкістю {movement_speed} м/сек, \
і подолав відстань {round(distance, 2)} метрів'

    # if time_movement < 0 or movement_speed < 0 or car_weight < 0:
    #     raise ValueError

    if '-' in result_message:

        raise ValueError('Wrong data')

    return result_message

