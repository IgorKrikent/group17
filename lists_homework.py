cities = ("6..58київ\n"
          "оДеса     Львів\tжитоМИР      уЖгОрОд ХарКІВ       слАвУтИч74$:?$")

for char in cities:

    if not char.isalpha():
        cities = cities.replace(f'{char}', ' ')

cities_list = cities.title().split()

for city in cities_list:

    if city[-1] == 'а':

        city = f'{city.strip('а')}у'

    print(f'Я \U00002764 {city}')

