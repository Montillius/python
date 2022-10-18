from pymongo import MongoClient


class MongoConfig:

    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017')
        self.db = self.client['dadospessoais']
        self.collection = self.db['users']

    def get_client(self):
        return self.client
    
    def get_db(self):
        return self.db
    
    def get_collection(self):
        return self.collection
    