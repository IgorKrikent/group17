import requests

from pprint import pprint

response = requests.get(url='https://dummyjson.com/carts')

data_from_net = response.json()

carts = data_from_net['carts']

# Использовал чтоб визуализировать структуру данных,
# в браузере/дебагере неудобно
# pprint(carts)

for cart in carts:

    if cart['userId'] == 56:

        for product in cart['products']:

            if product['discountPercentage'] > 15.0:

                print(product['title'])

