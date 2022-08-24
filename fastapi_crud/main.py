from fastapi import FastAPI


app = FastAPI()

# lista
classificacoes = []

# ROTA INICIAL 
@app.get('/')
def index():
    return {'Bem Vindo!': 'Esta é minha primera API'}








# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from typing import Optional, Text
# from datetime import datetime
# from uuid import uuid4 as uuid

# app = FastAPI()

# classificacoes = []


# class Tabela_model(BaseModel):
#     id: Optional[str]
#     posicao: str
#     time: str
#     created_at: datetime =  datetime.now()


# # index
# @app.get('/')
# def home():
#     return {"Bem vindo"}


# # vizualização geral
# @app.get('/tabela')
# def get_classificacao():
#     return classificacoes


# # vizualizar único
# @app.get('/tabela/{id}')
# def get_classificacao(id: str):
#     for classificacao in classificacoes:
#         if classificacao["id"] == id:
#             return classificacao
#     raise HTTPException(status_code=404, detail="Item não encontrado")


# # cadastrar
# @app.post('/tabela/cadastrar')
# def save_classificacao(dados: Tabela_model):
#     dados.id = str(uuid())
#     classificacoes.append(dados.dict())
#     return dados[-1]


# # editar
# @app.put('/tabela/{id}')
# def update_classificacao(id: str, update_classificacao: Tabela_model):
#     for index, classificacao in enumerate(classificacoes):
#         if classificacao["id"] == id:
#             classificacoes[index]["posicao"]= update_classificacao.dict()["posicao"]
#             classificacoes[index]["time"]= update_classificacao.dict()["time"]
#             return {"mensagen": "A postagem foi atualizada com sucesso"}
#     raise HTTPException(status_code=404, detail="Item não encontrado")


# # excluir
# @app.delete('/tabela/{id}')
# def delete_classificacao(id: str):
#     for index, classificacao in enumerate(classificacoes):
#         if classificacao["id"] == id:
#             classificacoes.pop(index)
#             return {"mensagen": "A postagem foi excluída com sucesso"}
#     raise HTTPException(status_code=404, detail="Item não encontrado")


