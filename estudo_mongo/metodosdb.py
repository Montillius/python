from hashlib import new
from turtle import update
from connection import MongoConfig

class MetodosMongo:

    def __init__(self):
        self.config = MongoConfig()
        self.collection = self.config.get_collection()
        self.db = self.config.db
        
    def insert_one(self, dados):
        try:
            result = self.collection.insert_one(dados)
            print(result)
        except Exception:
            raise Exception


    def insert_many(self, dados):
        try:
            result = self.collection.insert_many(dados)
            print(result)
        except Exception:
            raise Exception
        
    def find_one(self, dados):
        try:
            result = self.collection.find_one(dados)
            print(result)
        except Exception:
            raise Exception
   
    def find_all(self, dados):
        try:
            result = self.collection.find(dados)
            return print(result)
        except Exception:
            raise Exception
        
    def delete_one(self, dados):
        try:
            self.collection.delete_one(dados)
        except Exception:
            raise Exception    


    def delete_many(self, dados):
        try:
            result = self.collection.delete_many(dados)
            return print(result.deleted_count)
        except Exception:
            raise Exception
    
    def delete_all(self):
        try:
            result = self.collection.delete_many({})
            return print(result.deleted_count)
        except Exception:
            raise Exception
    
    def update_one(self, consulta, new_dados):
        try:
            update = { "$set": new_dados} 
            result = self.collection.update_one(consulta, update)
            print(result)
        except Exception:
            raise Exception
        
    def update_many(self, consulta, new_dados):
        try:
            update = { "$set": new_dados}
            result = self.collection.update_many(consulta, update)
            print(result)
        except Exception:
            raise Exception    
