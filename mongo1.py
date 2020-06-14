import pymongo
from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client['database']
collection = db['cities']
myquery = [
    {'_id':1,'name':'ongole','state':'ap'},
    {'_id':2,'name':'guntur','state':'ap'},
    {'_id':3,'name':'vizag','state':'ap'},
    {'_id':4,'name':'vijayawada','state':'ap'},
    {'_id':5,'name':'nellore','state':'ap'},
    {'_id':6,'name':'hydearabad','state':'ts'},
    {'_id':7,'name':'bangalore','state':'ka'},
    {'_id':8,'name':'chennai','state':'tn'},
    {'_id':9,'name':'mumbai','state':'mh'},
    {'_id':10,'name':'tiruvanthapuram','state':'ke'},
    {'_id':11,'name':'panaji','state':'go'},
    {'_id':12,'name':'gandhinagar','state':'gu'}
]
ins = collection.insert_many(myquery)
data = ins.find_many()
print(data)

