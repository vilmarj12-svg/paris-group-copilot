"""Endpoints do domínio Hipótese de Valor."""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/hipoteses", tags=["hipoteses"])


@router.post("", response_model=schemas.HipoteseRead, status_code=status.HTTP_201_CREATED)
def criar_hipotese(payload: schemas.HipoteseCreate, db: Session = Depends(get_db)):
    if db.get(models.Projeto, payload.projeto_id) is None:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    hipotese = models.Hipotese(**payload.model_dump())
    db.add(hipotese)
    db.commit()
    db.refresh(hipotese)
    return hipotese


@router.get("", response_model=list[schemas.HipoteseRead])
def listar_hipoteses(db: Session = Depends(get_db)):
    return db.query(models.Hipotese).all()
