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


class AlbumBase(BaseModel):
    titulo: str
    anio: int
    descripcion: str
    medio: Medio


class AlbumSchema(AlbumBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

    @field_serializer("medio")
    def serialize_medio(self, medio: Medio):
        if medio is None:
            return None
        return {"llave": medio.name, "valor": medio.value}


class AlbumCreateSchema(AlbumBase):
    pass


class AlbumUpdateSchema(AlbumBase):
    titulo: Optional[str] = None
    anio: Optional[int] = None
    descripcion: Optional[str] = None


class UsuarioBase(BaseModel):
    nombre_usuario: str
    contrasena: str


class UsuarioSchema(UsuarioBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class UsuarioCreateSchema(UsuarioBase):
    pass


class UsuarioUpdateSchema(UsuarioBase):
    nombre_usuario: Optional[str] = None
    contrasena: Optional[str] = None


class LoginSchema(BaseModel):
    nombre_usuario: str
    contrasena: str


class TokenSchema(BaseModel):
    access_token: str
    token_type: str
