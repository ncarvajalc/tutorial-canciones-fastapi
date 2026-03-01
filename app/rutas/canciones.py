from http import HTTPStatus
from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.esquemas import CancionCreateSchema, CancionSchema
from app.modelos import Cancion


router = APIRouter(prefix="/canciones", tags=["canciones"])


@router.post("/", response_model=CancionSchema, status_code=201)
def crear_cancion(cancion: CancionCreateSchema, db: Session = Depends(get_db)):
    db_cancion = Cancion(**cancion.model_dump())
    db.add(db_cancion)
    db.commit()
    db.refresh(db_cancion)
    return db_cancion

@router.get("/", response_model=list[CancionSchema])
def obtener_canciones(db: Session = Depends(get_db)):
    return db.query(Cancion).all()

@router.get("/{cancion_id}", response_model=CancionSchema)
def obtener_cancion(cancion_id: int, db: Session = Depends(get_db)):
    db_cancion = db.query(Cancion).filter(Cancion.id == cancion_id).first()
    if db_cancion is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Canción no encontrada")
    return db_cancion