from fastapi import FastAPI
from routes.rotas import table

app = FastAPI(title='Api with FastAPI and MongoDb',
              description='Projeto inicial de API com MongoDb e web scraping',
              version='0.0.1')

app.include_router(table)