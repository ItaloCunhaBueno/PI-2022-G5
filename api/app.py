from pprint import pprint

from models import Mensagens
from robyn import Headers, Request, Response, Robyn, jsonify
from sqlmodel import Session, SQLModel, create_engine

app = Robyn(__file__)

engine = create_engine("sqlite:///api/database.db")
SQLModel.metadata.create_all(bind=engine)

@app.get("/")
def index():
    """ENDPOINT PRINCIPAL."""
    return "Hello World"

@app.post("/api/novamensagem")
def nova_mensagem(request: Request):
    """ENDPOINT PARA ENVIAR UMA NOVA MENSAGEM."""
    pprint(request.json()["nome"])
    # print(request.body.to_dict())

    # valores = request.json()
    # print(valores)
    # nome =
    # email =
    # telefone =
    # texto =
    # mensagem = Mensagens(nome=nome, email=email, telefone=telefone, texto=texto)

    # with Session(engine) as session:
    #     session.add(mensagem)
    #     session.commit()
    return Response(status_code=200, headers=Headers({}), description="Mensagem enviada com sucesso!")


if __name__ == "__main__":
    # create a configured "Session" class
    app.start(port=7894)
