import os

import yagmail
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Mensagens
from sqlmodel import Session, SQLModel, create_engine

DB_URL = os.environ.get("SQL_ALCHEMY_URL")
FROM_EMAIL = os.environ.get("FROM_EMAIL")
TO_EMAIL = os.environ.get("TO_EMAIL") or FROM_EMAIL
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

app = FastAPI()
origins = ["*"]
app.add_middleware(
    middleware_class=CORSMiddleware,
    expose_headers=["*"],
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = create_engine(DB_URL)

SQLModel.metadata.create_all(bind=engine)


def enviar_email(mensagem: Mensagens):
    try:
        yag = yagmail.SMTP(FROM_EMAIL, EMAIL_PASSWORD)

        body = f"Você recebeu uma nova mensagem!\n\nConteúdo: {mensagem.texto}"

        yag.send(to=TO_EMAIL, subject="Você recebeu uma nova mensagem", contents=body)
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
        raise HTTPException(status_code=500, detail="Erro ao enviar e-mail")


@app.get("/api/teste")
async def index():
    """ENDPOINT PRINCIPAL."""
    return "API"


@app.post("/api/novamensagem")
async def nova_mensagem(mensagem: Mensagens):
    """ENDPOINT PARA ENVIAR UMA NOVA MENSAGEM."""
    with Session(engine) as session:
        session.add(mensagem)
        enviar_email(mensagem)
        session.commit()

    return {"status": 200, "mensagem": "Mensagem enviada com sucesso!"}


# if __name__ == "__main__":
#     from uvicorn import run
#     run("app:app", port=6789, log_level="info", reload=True)
