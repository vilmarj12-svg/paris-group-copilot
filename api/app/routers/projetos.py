"""Endpoints do domínio Projeto."""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/projetos", tags=["projetos"])


@router.post("", response_model=schemas.ProjetoRead, status_code=status.HTTP_201_CREATED)
def criar_projeto(payload: schemas.ProjetoCreate, db: Session = Depends(get_db)):
    projeto = models.Projeto(**payload.model_dump())
    db.add(projeto)
    db.commit()
    db.refresh(projeto)
    return projeto


@router.get("", response_model=list[schemas.ProjetoRead])
def listar_projetos(db: Session = Depends(get_db)):
    return db.query(models.Projeto).all()


@router.get("/{projeto_id}", response_model=schemas.ProjetoRead)
def obter_projeto(projeto_id: int, db: Session = Depends(get_db)):
    projeto = db.get(models.Projeto, projeto_id)
    if projeto is None:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    return projeto
