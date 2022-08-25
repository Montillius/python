from fastapi import APIRouter
from config.db import conexao
from models.classificacoes_model import Classificacao_model
from schemas.classificacao_schema import classificacao, tabela_classificacao

table = APIRouter()


# visualizar
@table.get('/tabela')
def find_all_classificacao():
    return tabela_classificacao(conexao.local.classificacoes.find())

# visualizar único
@table.get('/tabela/{id}')
def find_classificacao():
    return {'Bem Vindo!': 'Esta é minha primera API com Mongo'}

# cadastrar
@table.post('/tabela')
def create_classificacao(dados: Classificacao_model):
    nova_classificacao = dict(dados)
    id = conexao.local.classificacoes.insert_one(nova_classificacao).inserted_id

    return str(id)
# editar
@table.put('/tabela/{id}')
def update_classificacao():
    return {'Bem Vindo!': 'Esta é minha primera API com Mongo'}

# excluir
@table.delete('/tabela/{id}')
def delete_classificacao():
    return {'Bem Vindo!': 'Esta é minha primera API com Mongo'}