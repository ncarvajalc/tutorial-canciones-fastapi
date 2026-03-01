from fastapi import APIRouter
from microservicio_2.app.esquemas import CancionSchema
from microservicio_2.app.modelos import Cancion
from sqlalchemy.orm import Session
from fastapi.params import Depends
from microservicio_2.app.core.db import get_db

router = APIRouter(prefix="/canciones", tags=["canciones"])


@router.get("/tabla-puntajes", response_model=list[CancionSchema])
def obtener_tabla_puntajes(db: Session = Depends(get_db)):
    return db.query(Cancion).all()
