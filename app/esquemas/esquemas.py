from typing import Optional
from pydantic import BaseModel, ConfigDict, field_serializer

from app.modelos.modelos import Medio


class CancionBase(BaseModel):
    titulo: str
    minutos: int
    segundos: int
    interprete: str


class CancionCreateSchema(CancionBase):
    pass


class CancionUpdateSchema(CancionBase):
    titulo: Optional[str] = None
    minutos: Optional[int] = None
    segundos: Optional[int] = None
    interprete: Optional[str] = None


class CancionSchema(CancionBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class AlbumSchema(BaseModel):
    id: int
    titulo: str
    anio: int
    descripcion: str
    medio: Medio
    usuario_id: int

    model_config = ConfigDict(from_attributes=True)

    @field_serializer("medio")
    def serialize_medio(self, medio: Medio):
        if medio is None:
            return None
        return {"llave": medio.name, "valor": medio.value}


class UsuarioSchema(BaseModel):
    id: int
    nombre_usuario: str
    contrasena: str

    model_config = ConfigDict(from_attributes=True)
