from sqlmodel import Field, SQLModel


class Mensagens(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    telefone: str
    email: str
    texto: str
