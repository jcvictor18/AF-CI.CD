import sys
import os

# Adicionar o diretório 'app' ao caminho de busca do Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

@app.get("/saudacao/{nome}")
async def saudacao(nome: str):
    return {"mensagem": f"Olá, {nome}!"}
