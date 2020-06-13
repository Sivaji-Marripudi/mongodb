import pymongo
from pymongo import MongoClient
from pprint import pprint
client = MongoClient('localhost',27017)
pprint(client)
db = client.test
db.sites.insert_one({'url':'https://www.python.org','name':'python documentation'})
site = db.sites.find_one()
pprint(site)
