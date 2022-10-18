import collections
from http import client
from pymongo import MongoClient

# conexao com o mongo
client = MongoClient('mongodb://localhost:27017')

# banco
db = client['dadospessoais']

# collection
users = db['users']

# documento
user = {
    '_id': 1,
    'nome': 'João',
    'sobrenome':'fulano de tal'
}

# insert one
# view = users.insert_one(user)
# print(view)

# insert one com id
# view = users.insert_one(user).inserted_id
# print(view)


# insert many id autocomplete
userlist = [
  { "nome": "Amy", "sobrenome": "Apple st 652"},
  { "nome": "Hannah", "sobrenome": "Mountain 21"},
  { "nome": "Michael", "sobrenome": "Valley 345"},
  { "nome": "Sandy", "sobrenome": "Ocean blvd 2"},
  { "nome": "Betty", "sobrenome": "Green Grass 1"},
  { "nome": "Richard", "sobrenome": "Sky st 331"},
  { "nome": "Susan", "sobrenome": "One way 98"},
  { "nome": "Vicky", "sobrenome": "Yellow Garden 2"},
  { "nome": "Ben", "sobrenome": "Park Lane 38"},
  { "nome": "William", "sobrenome": "Central st 954"},
  { "nome": "Chuck", "sobrenome": "Main Road 989"},
  { "nome": "Viola", "sobrenome": "Sideway 1633"}
]
# view = users.insert_many(userlist).inserted_ids
# print(view)



# insert many com  id  específicos
userlistid = [
  { "_id": 1, "nome": "John", "sobrenome": "Highway 37"},
  { "_id": 2, "nome": "Peter", "sobrenome": "Lowstreet 27"},
  { "_id": 3, "nome": "Amy", "sobrenome": "Apple st 652"},
  { "_id": 4, "nome": "Hannah", "sobrenome": "Mountain 21"},
  { "_id": 5, "nome": "Michael", "sobrenome": "Valley 345"},
  { "_id": 6, "nome": "Sandy", "sobrenome": "Ocean blvd 2"},
  { "_id": 7, "nome": "Betty", "sobrenome": "Green Grass 1"},
  { "_id": 8, "nome": "Richard", "sobrenome": "Sky st 331"},
  { "_id": 9, "nome": "Susan", "sobrenome": "One way 98"},
  { "_id": 10, "nome": "Vicky", "sobrenome": "Yellow Garden 2"},
  { "_id": 11, "nome": "Ben", "sobrenome": "Park Lane 38"},
  { "_id": 12, "nome": "William", "sobrenome": "Central st 954"},
  { "_id": 13, "nome": "Chuck", "sobrenome": "Main Road 989"},
  { "_id": 14, "nome": "Viola", "sobrenome": "Sideway 1633"}
]

# view = users.insert_many(userlistid).inserted_ids
# print(view)

# find one
# view = users.find_one()
# print(view)

# find all
# for view in users.find({'nome':'Amy'}):
#     print(view)

# find all com restrição no return
# for view in users.find({},{'_id': 0, 'sobrenome': 0}):
#   print(view)

# find all com filtro
# consulta = { "sobrenome": "Park Lane 38" }
# results = users.find(consulta)
# for view in results:
#   print(view)

# find all com filtro mais complexo
# consulta = { "sobrenome": { "$regex": "^S" } }
# results = users.find(consulta)
# for view in results:
#     print(view)


# find all com ordenação por atributo
# results = users.find().sort("nome", 1)
# for view in results:
#   print(view)


# delete one 
# consulta = { "_id": 4 }
# users.delete_one(consulta)


# delete many
# consulta = { "sobrenome": {"$regex": "^S"} }
# view = users.delete_many(consulta)
# print(view.deleted_count, " total de documentos deletados.")

# delete all
# view = users.delete_many({})
# print(view.deleted_count, " total de documentos deletados.")


# drop collections
# users.drop()


# update one
# consulta = { '_id': 1 }
# update = { "$set": { 'nome': 'Pereirão' } }
# users.update_one(consulta, update)
# view = users.find_one({ 'nome': 'Pereirão' })
# print(view)


# update many
# consulta = { "sobrenome": { "$regex": "^A" } }
# update = { "$set": { "nome": "Joca" } }
# view = users.update_many(consulta, update)
# print("total de docmentos alterados ", view.modified_count)


# consulta com limit
# result = users.find().limit(5)
# for view in result:
#   print(view)