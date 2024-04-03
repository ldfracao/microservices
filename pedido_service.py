from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

origins = [
    'http://localhost:8004'
]

app.addmiddleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Pedido(BaseModel):
    user_id: int
    status: str
    order_id: int


@app.post("/pedido/{user_id}/add")
async def criar_pedido(pedido: Pedido):
    try:
        pedido_data = {
            "user_id": pedido.user_id,
            "status": pedido.status,
            "order_id": pedido.order_id
        }
        with open("pedido_data.txt", "w") as file:
            json.dump(pedido_data, file)
        return {"status": "sucesso", "mensagem": "Pedido criado", "order_id": {pedido.order_id}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/pedido/{user_id}/add")
async def obter_pedido():
    try:
        with open("pedido_data.txt", "r") as file:
            pedido_data = file.readlines()
        return {"pedido_data": pedido_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
