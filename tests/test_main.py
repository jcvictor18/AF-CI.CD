import sys
import os
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Bem-vindo ao app FastAPI com CI/CD!"}

def test_saudacao():
    response = client.get("/saudacao/Ana")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Olá, Ana!"}

def test_read_root_status_code():
    response = client.get("/")
    assert response.status_code == 200

def test_saudacao_conteudo():
    nome = "Carlos"
    response = client.get(f"/saudacao/{nome}")
    assert response.json()["mensagem"] == f"Olá, {nome}!"

def test_saudacao_status_code():
    response = client.get(f"/saudacao/")
    assert response.status_code == 200
