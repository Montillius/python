from fastapi import APIRouter, Response, status
from src.scraping import champion_italy

table = APIRouter()

# scraping
@table.get('/tabela/campeonato_italiano', tags=['scraper'])
def get_scraping():
    return champion_italy()