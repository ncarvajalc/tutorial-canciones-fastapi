from fastapi import APIRouter, HTTPException
from http import HTTPStatus
from app.esquemas import CancionCreateSchema, CancionSchema
from app.modelos import Cancion
from sqlalchemy.orm import Session
from fastapi.params import Depends
from app.core.db import get_db
from app.modelos.modelos import Album

router = APIRouter(prefix="/albumes", tags=["albumes"])


@router.post(
    "/{album_id}/canciones",
    response_model=CancionSchema,
    status_code=HTTPStatus.CREATED,
)
def asociar_cancion_a_album(
    album_id: int, cancion: CancionCreateSchema, db: Session = Depends(get_db)
):
    db_album = db.query(Album).filter(Album.id == album_id).first()
    if db_album is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Album no encontrado"
        )
    db_cancion = Cancion(**cancion.model_dump())
    db_album.canciones.append(db_cancion)
    db.commit()
    db.refresh(db_cancion)
    return db_cancion


@router.get("/{album_id}/canciones", response_model=list[CancionSchema])
def obtener_canciones_de_album(album_id: int, db: Session = Depends(get_db)):
    db_album = db.query(Album).filter(Album.id == album_id).first()
    if db_album is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Album no encontrado"
        )
    return db_album.canciones
