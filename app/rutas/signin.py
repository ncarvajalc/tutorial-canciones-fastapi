from fastapi import APIRouter, HTTPException
from http import HTTPStatus
from app.esquemas import UsuarioCreateSchema, UsuarioSchema, UsuarioUpdateSchema
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


@router.put("/{usuario_id}", response_model=UsuarioSchema)
def actualizar_usuario(
    usuario_id: int, usuario: UsuarioUpdateSchema, db: Session = Depends(get_db)
):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if db_usuario is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Usuario no encontrado"
        )
    data = usuario.model_dump(exclude_unset=True)
    for key, value in data.items():
        setattr(db_usuario, key, value)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario
