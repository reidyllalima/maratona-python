from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/piadas/{numero_de_piadas}")
async def retorna_piadas(numero_de_piadas: int):
    lista_de_piadas = []
    for i in range(numero_de_piadas):
        response_piadas = requests.get("https://api.chucknorris.io/jokes/random")
        if response_piadas.status_code == 200:
            dado = response_piadas.json()
            piada = dado["value"]
            lista_de_piadas.append(piada)
    return {"message": lista_de_piadas}

@app.get("/piadas/categoria/{categoria_da_piada}")
async def retorna_piadas(categoria_da_piada: str):
        response_piadas = requests.get(f"https://api.chucknorris.io/jokes/random?category={categoria_da_piada}")
        if response_piadas.status_code == 200:
            dado = response_piadas.json()
            piada = dado["value"]
        return {"message": piada} 




