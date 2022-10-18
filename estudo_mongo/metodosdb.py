from connection import MongoConfig
import json

class MetodosMongo:

    def __init__(self):
        self.config = MongoConfig()
        self.collection = self.config.get_collection()
        dados = self.get_dados
        
        
        
    def get_dados(self):
        try:
            with open('biblioteca.json', 'r') as json_file:
                dados = json.load(json_file)
            return dados
        except Exception:
            raise Exception


    def insert_one(self, dados):
        try:
            result = self.collection.insert_one(dados)
            return print(result)
        except Exception:
            raise Exception

