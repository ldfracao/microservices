from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

app = FastAPI()

class Cart(BaseModel):
    user_id: int
    produto_id: int
    quantidade: int

@app.post("/carrinho/{user_id}/add")
async def add_carrinho(cart: Cart):
    try:
        cart_data = {
            "user_id": cart.user_id,
            "produto_id": cart.produto_id,
            "quantidade": cart.quantidade
        }

        with open("cart_data.txt", "w") as file:
            json.dump(cart_data, file)
        return {"status": "sucesso", "mensagem": "Produto adicionado ao carrinho"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/carrinho/{user_id}/add")
async def obter_carrinho():
    try:
        with open("cart_data.txt") as file:
            cart_data = file.readlines()
        return {"cart_data": cart_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
