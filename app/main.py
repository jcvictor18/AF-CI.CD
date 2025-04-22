from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "Bem-vindo ao app FastAPI com CI/CD!"}

@app.get("/saudacao/{nome}")
def saudacao(nome: str):
    return {"mensagem": f"Olá, {nome}!"}
