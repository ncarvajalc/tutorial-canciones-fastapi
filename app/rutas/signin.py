from fastapi import APIRouter
from http import HTTPStatus
from app.esquemas import UsuarioCreateSchema, UsuarioSchema
from app.modelos import Usuario
from sqlalchemy.orm import Session
from fastapi.params import Depends
from app.core.db import get_db

router = APIRouter(prefix="/signin", tags=["signin"])


@router.post("/", response_model=UsuarioSchema, status_code=HTTPStatus.CREATED)
def crear_usuario(usuario: UsuarioCreateSchema, db: Session = Depends(get_db)):
    db_usuario = Usuario(**usuario.model_dump())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario
