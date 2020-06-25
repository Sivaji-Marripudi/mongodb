import pymongo
from pymongo import MongoClient
client = MongoClient('localhost',27017)
database = client['mydata']
collection = database['posts']
query = [
    {
        '_id':1,
        'name':'siva',
        'url':'https://www.sivaji.com',
        'email':'siva@gmail.com',
        'phone':9988776655,
        'address':{
            'village':'abc',
            'mandal':'dhgs',
            'city':'newyork'
        },
        'hobbies':['cooking','dancing','reading']
    },
    {
        '_id':2,
        'name':'ram',
        'url':'https://www.ram.com',
        'email':'ram@gmail.com',
        'phone':9988776654,
        'address':{
            'village':'abc',
            'mandal':'dhgs',
            'city':'newyork'
        },
        'hobbies':['playing','cooking','dancing','reading']
    },
    {
        '_id':3,
        'name':'krishna',
        'url':'https://www.krishna.com',
        'email':'kriasn@gmail.com',
        'phone':9988776653,
        'address':{
            'village':'abc',
            'mandal':'dhgs',
            'city':'newyork'
        },
        'hobbies':['playing','cooking','reading']
    },
    {
        '_id':4,
        'name':'venkat',
        'url':'https://www.venkat.com',
        'email':'venkat@gmail.com',
        'phone':9988776644,
        'address':{
            'village':'abc',
            'mandal':'dhgs',
            'city':'newyork'
        },
        'hobbies':['playing','cooking','cycling','reading']
    },
    {
        '_id':5,
        'name':'bhai',
        'url':'https://www.bhai.com',
        'email':'bhai@gmail.com',
        'phone':9988776622,
        'address':{
            'village':'abc',
            'mandal':'dhgs',
            'city':'newyork'
        },
        'hobbies':['playing','cooking','reading']
    }
]
insert = collection.insert_one(query)
print(insert)
