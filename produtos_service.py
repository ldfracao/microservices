from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

app = FastAPI()

class Produto(BaseModel):
    id: int
    nome: str
    preco: float

@app.post("/produtos")
async def save_produtos(produtos: Produto):
    try:
        produtos_data = {
            "id": produtos.id,
            "nome": produtos.nome,
            "preco": produtos.preco
        }
        with open("produtos_data.txt", "w") as file:
                json.dump(produtos_data, file)
        return {"status": "sucesso", "mensagem": "Produtos salvos no arquivo"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/produtos")
async def list_produtos():
    try:
        with open("produtos_data.txt", "r") as file:
            produtos_data = file.readlines()
        return {"produtos_data": produtos_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
