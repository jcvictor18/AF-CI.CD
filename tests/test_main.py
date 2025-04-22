from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Bem-vindo ao app FastAPI com CI/CD!"}

def test_saudacao():
    response = client.get("/saudacao/Ana")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Olá, Ana!"}
