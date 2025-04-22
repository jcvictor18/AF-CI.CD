import sys
import os
from fastapi.testclient import TestClient

# Adicionar o diretório 'app' ao caminho de busca do Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

<<<<<<< HEAD
import pytest
from fastapi.testclient import TestClient
from app.main import app  # Certifique-se de que o caminho está correto
=======
from main import app
>>>>>>> ba1d5c5 (Configuração do workflow do GitHub Actions com FastAPI e testes)

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Bem-vindo ao app FastAPI com CI/CD!"}

def test_saudacao():
    response = client.get("/saudacao/Ana")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Olá, Ana!"}

