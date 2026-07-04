"""Aplicação FastAPI do Paris Group Copilot.

Expõe o contrato OpenAPI automaticamente em /docs e /openapi.json.
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI

from .database import init_db
from .routers import hipoteses, projetos


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Paris Group Copilot API",
    description="Backend de discovery e execução de MVPs com IA em venture studio.",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(projetos.router)
app.include_router(hipoteses.router)


@app.get("/health", tags=["infra"])
def health():
    return {"status": "ok"}
