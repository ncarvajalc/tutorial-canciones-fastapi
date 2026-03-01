from fastapi import APIRouter, HTTPException
from http import HTTPStatus

from sqlalchemy.exc import IntegrityError
from app.esquemas import AlbumCreateSchema, AlbumSchema
from app.modelos import Album
from sqlalchemy.orm import Session
from fastapi.params import Depends
from app.core.db import get_db
from app.core.seguridad import verificar_token

router = APIRouter(prefix="/usuarios", tags=["usuarios"])


@router.post("/me/albumes", response_model=AlbumSchema, status_code=HTTPStatus.CREATED)
def crear_album(
    album: AlbumCreateSchema,
    db: Session = Depends(get_db),
    usuario_id: int = Depends(verificar_token),
):
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


@router.get("/me/albumes", response_model=list[AlbumSchema])
def obtener_albumes(
    db: Session = Depends(get_db),
    usuario_id: int = Depends(verificar_token),
):
    return db.query(Album).filter(Album.usuario_id == usuario_id).all()
