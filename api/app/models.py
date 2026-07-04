"""Modelos de persistência do Paris Group Copilot.

Duas entidades centrais do domínio de discovery de venture studio:
- Projeto: um MVP/produto em exploração no studio.
- Hipotese: a hipótese de valor testável associada a um projeto.
"""
from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


class Projeto(Base):
    __tablename__ = "projetos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(200), nullable=False)
    descricao: Mapped[str] = mapped_column(Text, default="")

    hipoteses: Mapped[list["Hipotese"]] = relationship(
        back_populates="projeto", cascade="all, delete-orphan"
    )


class Hipotese(Base):
    __tablename__ = "hipoteses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    projeto_id: Mapped[int] = mapped_column(
        ForeignKey("projetos.id", ondelete="CASCADE"), nullable=False
    )
    # Enunciado no formato causal: "Se ..., então ..., porque ..."
    enunciado: Mapped[str] = mapped_column(Text, nullable=False)
    # Critério de aceitação quantitativo, ex: "tempo médio < 10 min em 5 testes"
    metrica_sucesso: Mapped[str] = mapped_column(String(300), nullable=False)

    projeto: Mapped["Projeto"] = relationship(back_populates="hipoteses")
