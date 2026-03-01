from fastapi import APIRouter, HTTPException
from http import HTTPStatus

from sqlalchemy.exc import IntegrityError
from app.esquemas import AlbumCreateSchema, AlbumSchema
from app.modelos import Album, Usuario
from sqlalchemy.orm import Session
from fastapi.params import Depends
from app.core.db import get_db

router = APIRouter(prefix="/usuarios", tags=["usuarios"])


@router.post(
    "/{usuario_id}/albumes", response_model=AlbumSchema, status_code=HTTPStatus.CREATED
)
def crear_album(
    usuario_id: int, album: AlbumCreateSchema, db: Session = Depends(get_db)
):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if db_usuario is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Usuario no encontrado"
        )
    try:
        db_album = Album(**album.model_dump(), usuario_id=usuario_id)
        db.add(db_album)
        db.commit()
        db.refresh(db_album)
        return db_album
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail="El usuario ya tiene un album con dicho nombre",
        )


@router.get("/{usuario_id}/albumes", response_model=list[AlbumSchema])
def obtener_albumes(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if db_usuario is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Usuario no encontrado"
        )
    return db_usuario.albumes
