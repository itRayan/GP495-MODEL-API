from fastapi import FastAPI
from utils import database

app = FastAPI()

@app.get('/')
async def readSchema():
    return database.extractSchema()