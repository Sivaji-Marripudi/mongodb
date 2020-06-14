try:
    import json
    import pymongo
    from pymongo import MongoClient
    import pandas as pd
except Exception as e:
    print('some modules are missing......buddy')
class mongodb(object):
    def __init__(self,dbname,collectionname):
        self.dbname = dbname
        self.collectionname = collectionname
        self.client = MongoClient('localhost',27017)
        self.database = self.client['dbname']
        self.collection = self.database['collectionname']
    def inserted(self,path = None):
        df = pd.read_csv(path)
        data = df.to_dict('records')
        self.collection.insert_many(data)
        print('successfully exported')
if __name__ == '__main__':
    mongo = mongodb(dbname = 'dataset',collectionname = 'csvfile')
    mongo.inserted(path = 'data.csv')
