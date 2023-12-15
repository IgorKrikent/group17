import requests
import json

url = 'https://dummyjson.com/quotes?limit=100'

response = requests.get(url=url)

data_from_net = response.json()

with open('data_from_net.json', 'w', encoding='utf-8') as file:

    json.dump(data_from_net, file, indent=4)

json_string = json.dumps(data_from_net, indent=4)

print(json_string)

