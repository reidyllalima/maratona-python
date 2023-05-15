from fastapi import FastAPI, Form, Response
from datetime import datetime
from request import retorna_fotos
import pandas as pd

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


@app.get("/fotos")
async def fotos():
    fotos_nasa = retorna_fotos()
    return {"message": fotos_nasa}


@app.post("/excel")
async def excel(
    first_name: str = Form(...), last_name: str = Form(...), age: int = Form(...)
):
    data = {"Nome": [first_name], "Sobrenome": [last_name], "Idade": [age]}
    df = pd.DataFrame(data)

    file_name = f"{first_name}_{last_name}.xlsx"
    with pd.ExcelWriter(file_name) as writer:
        df.to_excel(writer, sheet_name="Dados do Usuário", index=False)

    with open(file_name, "rb") as file:
        contents = file.read()
        response = Response(content=contents, media_type="application/vnd.ms-excel")
        response.headers["Content-Disposition"] = f"attachment; filename={file_name}"
