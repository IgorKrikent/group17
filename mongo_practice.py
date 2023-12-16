from pprint import pprint

import pymongo
import requests
import config

url_mongo = 'mongodb+srv://{user}:{password}@clustertest.ivjzucs.mongodb.net/?retryWrites=true&w=majority'
url_mongo = url_mongo.format(user=config.USER, password=config.PASSWORD)

url_data_from_net = 'https://dummyjson.com/quotes?limit=100'

response = requests.get(url_data_from_net)

data_from_net = response.json()
quotes = data_from_net['quotes']

# pprint(quotes)

client = pymongo.MongoClient(url_mongo)

db = client['library']
quotes_collection = db['quotes']

quotes_collection.insert_many(quotes)

query = {"author": {"$regex": "Albert Einstein"}}
einstein_quotes = quotes_collection.find(query)

for quote in einstein_quotes:

    print(quote["quote"])

print("*"*50)

query = {"quote": {"$regex": "success "}}
motivation_quotes = quotes_collection.find(query)

for motivation_quote in motivation_quotes:

    print(motivation_quote["quote"])


query = {"author": {"$regex": "Mark Twain"}}
quotes_collection.update_many(query, {"$set": {"favorite": True}})

quotes_collection.delete_many({"author": {"$regex": "Vincent Van Gogh"}})

quotes_collection.delete_many({})

