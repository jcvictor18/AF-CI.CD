import sys
import os

# Adicionar o diretório 'app' ao caminho de busca do Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

import pytest
from fastapi.testclient import TestClient
from app.main import app  # Certifique-se de que o caminho está correto

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Bem-vindo ao app FastAPI com CI/CD!"}

def test_saudacao():
    response = client.get("/saudacao/Ana")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Olá, Ana!"}

