from typing import Optional

from sqlmodel import Field, SQLModel


class Mensagens(SQLModel, table=True):
    """CLASSE CONTENDO AS DEFINICOES DA TABELA DE MENSAGENS."""

    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str = Field(nullable=False)
    telefone: str = Field(nullable=False)
    email: Optional[str]
    texto: str = Field(nullable=False)
