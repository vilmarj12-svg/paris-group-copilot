"""Schemas Pydantic — a fonte de verdade do contrato OpenAPI.

O FastAPI gera o schema OpenAPI automaticamente a partir destes modelos.
O frontend Next.js consome esse contrato (em /openapi.json) para se manter
sincronizado com o backend sem acoplamento manual.
"""
from pydantic import BaseModel, ConfigDict, Field


class ProjetoCreate(BaseModel):
    nome: str = Field(..., examples=["Paris Group Copilot"])
    descricao: str = Field("", examples=["Copiloto de discovery de MVPs com IA"])


class ProjetoRead(ProjetoCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)


class HipoteseCreate(BaseModel):
    projeto_id: int = Field(..., examples=[1])
    enunciado: str = Field(
        ...,
        examples=[
            "Se o copiloto sugerir enquadramentos de MVPs anteriores, então a PM "
            "formula a hipótese mais rápido, porque reusa o aprendizado do studio."
        ],
    )
    metrica_sucesso: str = Field(
        ..., examples=["4 de 5 PMs formulam a hipótese em < 10 min"]
    )


class HipoteseRead(HipoteseCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)
