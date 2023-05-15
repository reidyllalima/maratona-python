from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hora")
async def data():
    now = datetime.now()
    return {"message": now}

@app.get("/nome/{nome}")
async def nome(nome: str):
    return {"message": f"Hello {nome}"}