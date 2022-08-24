from fastapi import APIRouter
from config.db import conexao

table = APIRouter()


# visualizar
@table.get('/tabela')
def find_all_classificacao():
    return {'Bem Vindo!': 'Esta é minha primera API com Mongo'}

# visualizar unico
@table.get('/tabela/{id}')
def find_classificacao():
    return {'Bem Vindo!': 'Esta é minha primera API com Mongo'}

# cadastrar
@table.post('/tabela')
def create_classificacao():
    return {'Bem Vindo!': 'Esta é minha primera API com Mongo'}

# editar
@table.put('/tabela/{id}')
def update_classificacao():
    return {'Bem Vindo!': 'Esta é minha primera API com Mongo'}

# excluir
@table.delete('/tabela/{id}')
def delete_classificacao():
    return {'Bem Vindo!': 'Esta é minha primera API com Mongo'}