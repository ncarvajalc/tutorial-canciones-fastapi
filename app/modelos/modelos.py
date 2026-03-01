from sqlalchemy import ForeignKey, String, Enum, Table, Column, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import enum


class Base(DeclarativeBase):
    pass


album_cancion = Table(
    "album_cancion",
    Base.metadata,
    Column("album_id", ForeignKey("albumes.id"), primary_key=True),
    Column("cancion_id", ForeignKey("canciones.id"), primary_key=True),
)


class Cancion(Base):
    __tablename__ = "canciones"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(128))
    minutos: Mapped[int] = mapped_column()
    segundos: Mapped[int] = mapped_column()
    interprete: Mapped[str] = mapped_column(String(128))

    albumes: Mapped[list["Album"]] = relationship(
        secondary=album_cancion,
        back_populates="canciones",
    )


class Medio(enum.Enum):
    DISCO = 1
    CASETE = 2
    CD = 3


class Album(Base):
    __tablename__ = "albumes"
    __table_args__ = (UniqueConstraint("usuario_id", "titulo", name="uq_album_usuario_titulo"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(128))
    anio: Mapped[int] = mapped_column()
    descripcion: Mapped[str] = mapped_column(String(512))
    medio: Mapped[Medio] = mapped_column(Enum(Medio))
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))

    usuario: Mapped["Usuario"] = relationship(back_populates="albumes")
    canciones: Mapped[list["Cancion"]] = relationship(
        secondary=album_cancion,
        back_populates="albumes",
    )


class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre_usuario: Mapped[str] = mapped_column(String(50))
    contrasena: Mapped[str] = mapped_column(String(50))
    albumes: Mapped[list["Album"]] = relationship(
        back_populates="usuario", cascade="all, delete-orphan"
    )
