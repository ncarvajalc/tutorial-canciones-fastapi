from fastapi import APIRouter, HTTPException, Response
from http import HTTPStatus
from app.esquemas import AlbumSchema, AlbumUpdateSchema
from app.modelos import Album
from sqlalchemy.orm import Session
from fastapi.params import Depends
from app.core.db import get_db

router = APIRouter(prefix="/albumes", tags=["albumes"])


@router.get("/{album_id}", response_model=AlbumSchema)
def obtener_album(album_id: int, db: Session = Depends(get_db)):
    db_album = db.query(Album).filter(Album.id == album_id).first()
    if db_album is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Album no encontrado"
        )
    return db_album


@router.put("/{album_id}", response_model=AlbumSchema)
def actualizar_album(
    album_id: int, album: AlbumUpdateSchema, db: Session = Depends(get_db)
):
    db_album = db.query(Album).filter(Album.id == album_id).first()
    if db_album is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Album no encontrado"
        )
    data = album.model_dump(exclude_unset=True)
    for key, value in data.items():
        setattr(db_album, key, value)
    db.commit()
    db.refresh(db_album)
    return db_album


@router.delete("/{album_id}", status_code=HTTPStatus.NO_CONTENT)
def eliminar_album(album_id: int, db: Session = Depends(get_db)):
    db_album = db.query(Album).filter(Album.id == album_id).first()
    if db_album is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Album no encontrado"
        )
    db.delete(db_album)
    db.commit()
    return Response(status_code=HTTPStatus.NO_CONTENT)
