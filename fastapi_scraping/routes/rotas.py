from fastapi import APIRouter
from src.scraping import champion_italy, champion_brazil, champion_english

table = APIRouter()

# scraping
@table.get('/tabela/campeonato_italiano', tags=['Campeonatos'])
def get_italy():
    return champion_italy()

# scraping
@table.get('/tabela/campeonato_brasileiro', tags=['Campeonatos'])
def get_brazil():
    return champion_brazil()

# scraping
@table.get('/tabela/campeonato_ingles', tags=['Campeonatos'])
def get_english():
    return champion_english()