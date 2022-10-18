from requests import delete
from metodosdb import MetodosMongo

if __name__ == '__main__':
    MetodosMongo = MetodosMongo()
    MetodosMongo.update_one({"_id":1}, {'nome':'teste'})