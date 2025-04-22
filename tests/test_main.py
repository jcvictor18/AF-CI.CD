import sys
import os

# Adicionar o diretório 'app' ao caminho de busca do Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Bem-vindo ao app FastAPI com CI/CD!"}

def test_saudacao():
    response = client.get("/saudacao/Ana")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Olá, Ana!"}
