from fastapi import APIRouter, HTTPException
from http import HTTPStatus
from app.esquemas import CancionSchema
from app.modelos import Cancion
from sqlalchemy.orm import Session
from fastapi.params import Depends
from app.core.db import get_db
from app.modelos.modelos import Album

router = APIRouter(prefix="/albumes", tags=["albumes"])


@router.post(
    "/{album_id}/canciones/{cancion_id}",
    response_model=CancionSchema,
    status_code=HTTPStatus.CREATED,
)
def asociar_cancion_a_album(
    album_id: int, cancion_id: int, db: Session = Depends(get_db)
):
    db_album = db.query(Album).filter(Album.id == album_id).first()
    if db_album is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Album no encontrado"
        )
    db_cancion = db.query(Cancion).filter(Cancion.id == cancion_id).first()
    if db_cancion is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Cancion no encontrada"
        )
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
