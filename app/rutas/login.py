from fastapi import APIRouter, HTTPException
from http import HTTPStatus
from app.esquemas import LoginSchema
from app.modelos import Usuario
from sqlalchemy.orm import Session
from fastapi.params import Depends
from app.core.db import get_db

router = APIRouter(prefix="/login", tags=["login"])


@router.post("/", status_code=HTTPStatus.OK)
def login(login: LoginSchema, db: Session = Depends(get_db)):
    db_usuario = (
        db.query(Usuario)
        .filter(
            (Usuario.nombre_usuario == login.nombre_usuario)
            & (Usuario.contrasena == login.contrasena)
        )
        .first()
    )
    if db_usuario is None:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail="Nombre de usuario o contraseña incorrectos",
        )
    return {"mensaje": "Inicio de sesión exitoso"}
