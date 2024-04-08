from sqlmodel import Field, SQLModel


class Mensagens(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(nullable=False)
    telefone: str | None
    email: str | None
    texto: str = Field(nullable=False)
