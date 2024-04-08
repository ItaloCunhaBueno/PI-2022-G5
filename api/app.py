
from pathlib import Path

from dotenv import dotenv_values
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Mensagens
from sqlmodel import Session, SQLModel, create_engine

ENV = dotenv_values(Path(Path(__file__).parent,".env"))
print(ENV)
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

# engine = create_engine("sqlite:///api/database.db")
engine = create_engine(ENV["CONNECTIONSTRING"])

SQLModel.metadata.create_all(bind=engine)

@app.get("/")
def index():
    """ENDPOINT PRINCIPAL."""
    return None

@app.post("/api/novamensagem")
def nova_mensagem(mensagem: Mensagens):
    """ENDPOINT PARA ENVIAR UMA NOVA MENSAGEM."""
    with Session(engine) as session:
        session.add(mensagem)
        session.commit()
    return {"status":200, "mensagem":"Mensagem enviada com sucesso!"}


if __name__ == "__main__":
    from uvicorn import run
    run("app:app", port=6789, log_level="info", reload=True)
