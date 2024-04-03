from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json

app = FastAPI()

origins = [
    'http://localhost:8001'
]

app.addmiddleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Login(BaseModel):
    username: str
    password: str


@app.post("/login/")
async def login(login: Login):
    try:
        login_data = {
            "username": login.username,
            "password": login.password
        }
        with open("login_data.txt", "w") as file:
            json.dump(login_data, file)
        return {"status": "sucesso", "mensagem": "Usuário autenticado"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/login/")
async def get_login_info():
    try:
        with open("login_data.txt", "r") as file:
            login_info = file.readlines()
        return {"login_info": login_info}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
