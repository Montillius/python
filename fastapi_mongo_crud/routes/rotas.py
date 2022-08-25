from fastapi import APIRouter, Response, status
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

from config.db import conexao
from models.classificacoes_model import Classificacao_model
from schemas.classificacao_schema import classificacao, tabela_classificacao


table = APIRouter()


# visualizar
@table.get('/users')
def find_all_classificacao():
    return tabela_classificacao(conexao.local.classificacoes.find())


# visualizar único
@table.get('/tabela/{id}')
def find_classificacao(id: str):
    return classificacao(conexao.local.classificacoes.find_one({'_id': ObjectId(id)}))


# cadastrar
@table.post('/tabela/cadastrar')
def create_classificacao(dados: Classificacao_model):
    nova_classificacao = dict(dados)
    del nova_classificacao['id']
    id = conexao.local.classificacoes.insert_one(nova_classificacao).inserted_id
    dados = conexao.local.classificacoes.find_one({'_id': id})
    return classificacao(dados)


# editar
@table.put('/tabela/editar/{id}')
def update_classificacao(id: str, dados: Classificacao_model):
    conexao.local.classificacoes.find_one_and_update(
        {'_id': ObjectId(id)}, {'$set': dict(dados)})
    return classificacao(conexao.local.classificacoes.find_one({'_id': ObjectId(id)}))

# excluir
@table.delete('/tabela/excluir/{id}', status_code = status.HTTP_204_NO_CONTENT, tags=['tabela_campeonato'])
def delete_classificacao(id: str):
    classificacao(conexao.local.classificacoes.find_one_and_delete({'_id': ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)
