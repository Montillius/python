from fastapi import FastAPI
from routes.rotas import table

app = FastAPI()

app.include_router(table)