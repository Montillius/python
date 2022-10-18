from metodosdb import MetodosMongo

if __name__ == '__main__':
    MetodosMongo = MetodosMongo()
    user = {
    'nome': 'João',
    'sobrenome':'fulano de tal'
    }
    MetodosMongo.insert_one(user)
