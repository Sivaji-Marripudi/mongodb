import json
import pymongo
from pymongo import MongoClient
client = MongoClient('localhost',27017)
database = client['dataset']
collection = database['states']
with open (r'data.json','r') as f:
    file_data = json.load(f)
final = collection.insert_one(file_data)
print('successfully completed')
client.close()