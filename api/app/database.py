"""Conexão com o PostgreSQL via SQLAlchemy.

O stack reutilizável do studio assume Postgres como banco relacional padrão.
A URL vem do ambiente (DATABASE_URL) — nunca hardcoded — para o mesmo código
rodar local, em CI e em produção sem alteração.
"""
import os
import time

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://copilot:copilot@localhost:5432/copilot",
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


def init_db() -> None:
    """Cria as tabelas, aguardando o Postgres ficar disponível.

    Em `docker compose up` o container da API pode subir antes do banco aceitar
    conexões. O retry evita um crash de boot por corrida de inicialização.
    """
    from . import models  # noqa: F401  (registra os modelos no metadata)

    last_error: Exception | None = None
    for _ in range(15):
        try:
            Base.metadata.create_all(bind=engine)
            return
        except Exception as exc:  # pragma: no cover - depende de infra
            last_error = exc
            time.sleep(2)
    if last_error:
        raise last_error


def get_db():
    """Dependency do FastAPI: abre e fecha a sessão por request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
