from pydantic import BaseModel
from typing import Optional

class Classificacao_model(BaseModel):
    id: Optional[str]
    posicao: str
    time: str
    pontos:int
    jogos: int      
    vitorias: int 
    empates: int 
    derrotas: int 
    gols_feitos: int 
    gols_sofridos: int 
    saldo_de_gols: int 
    aproveitamento: int 
    
    
