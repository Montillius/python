from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from uuid import uuid4 as uuid

app = FastAPI()

# lista
classificacoes = []

# model
class Classificacao_model(BaseModel):
    id: Optional[str]
    posicao: str
    time: str
    created_at: datetime = datetime.now()


# index
@app.get('/')
def index():
    return {'Bem Vindo!': 'Esta é minha primera API'}


# vizualizar lista
@app.get('/tabela')
def get_tabela():
    return classificacoes


# vizualizar único
@app.get('/tabela/{id_classificacao}')
def get_classificacao(id_classificacao: str):
    for classificacao in classificacoes:
        if classificacao['id'] == id_classificacao:
            return classificacao
    raise HTTPException(status_code=404, detail='Id não encontrado')

# cadastrar
@app.post('/tabela/cadastrar')
def save_classificacao(dados: Classificacao_model):
    dados.id = str(uuid())
    classificacoes.append(dados.dict())
    return classificacoes[-1]

# editar
@app.put('/tabela/{id_classificacao}')
def update_classificacao(id_classificacao: str, update_classificacao:Classificacao_model):
    for index, classificacao in enumerate(classificacoes):
        if classificacao['id'] == id_classificacao:
            classificacoes[index]['posicao'] = update_classificacao.posicao
            classificacoes[index]['time'] = update_classificacao.time
            return{'Mensagem':'A classificação foi editada com sucesso'}
    raise HTTPException(status_code=404, detail='Id não encontrado')

# excluir
@app.delete('/tabela/{id_classificacao}')
def delete_classificacao(id_classificacao: str):
        for index, classificacao in enumerate(classificacoes):
                if classificacao['id'] == id_classificacao:
                    classificacoes.pop(index)
                    return{'Mensagem':'A classificação foi deletada com sucesso'}
        raise HTTPException(status_code=404, detail='Id não encontrado')