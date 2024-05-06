
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Mensagens
from sqlmodel import Session, SQLModel, create_engine

DB_URL = os.environ.get("SQL_ALCHEMY_URL")

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    expose_headers=["*"],
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = create_engine(DB_URL)

SQLModel.metadata.create_all(bind=engine)

@app.get("/")
def index():
    """ENDPOINT PRINCIPAL."""
    return None

@app.post("/novamensagem")
def nova_mensagem(mensagem: Mensagens):
    """ENDPOINT PARA ENVIAR UMA NOVA MENSAGEM."""
    with Session(engine) as session:
        session.add(mensagem)
        session.commit()
    return {"status":200, "mensagem":"Mensagem enviada com sucesso!"}


if __name__ == "__main__":
    from uvicorn import run
    run("app:app", port=6789, log_level="info", reload=True)
