# Import Module
from pymongo import MongoClient
import json
 
# Create a MongoClient object on port 27017
client = MongoClient('localhost', 27017)
db = client['rental.json']
collection = db['rental']
result = collection.find_one()

#ugly but works
# print(result)

#pretty print the result
print(json.dumps(result, indent=4, default=str))

resault = collection.find()
for document in resault:
    print(json.dumps(document, indent=4, default=str))
client.close()