import pymongo
from pymongo import MongoClient
from pprint import pprint # pprint library is used to make the output look more pretty
client = MongoClient('localhost',27017) # connect to mongodb using MongoClient driver
print(client.list_database_names()) # how to check the database is already exists or not .
pprint(client)
db = client.test # created database 'test'
# create collection (table) and insert records to the collection
db.sites.insert_one({'url':'https://www.python.org','name':'python documentation'}) 
site = db.sites.find_one()
pprint(site)
