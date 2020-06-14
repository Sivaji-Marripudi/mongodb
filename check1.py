import pymongo
from pymongo import MongoClient
client = MongoClient('localhost',27017)
dbs = client.list_database_names()
print(dbs)
if 'mydata' in dbs:
    print('exists')
else:
    print('not exists')
