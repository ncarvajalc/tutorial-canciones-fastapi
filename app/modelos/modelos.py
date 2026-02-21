from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import enum
from sqlalchemy import Enum


class Base(DeclarativeBase):
    pass


class Cancion(Base):
    __tablename__ = "canciones"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(128))
    minutos: Mapped[int] = mapped_column()
    segundos: Mapped[int] = mapped_column()
    interprete: Mapped[str] = mapped_column(String(128))

    def __repr__(self):
        return "{},{},{},{}".format(
            self.titulo, self.minutos, self.segundos, self.interprete
        )


class Medio(enum.Enum):
    DISCO = 1
    CASETE = 2
    CD = 3


class Album(Base):
    __tablename__ = "albumes"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(128))
    anio: Mapped[int] = mapped_column()
    descripcion: Mapped[str] = mapped_column(String(512))
    medio: Mapped[Medio] = mapped_column(Enum(Medio))


class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre_usuario: Mapped[str] = mapped_column(String(50))
    contrasena: Mapped[str] = mapped_column(String(50))
