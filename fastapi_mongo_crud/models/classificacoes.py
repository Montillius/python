from pydantic import BaseModel

class Classificacoes(BaseModel):
    id: str
    posicao: str
    time: str
    