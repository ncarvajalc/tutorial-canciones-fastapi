from sqlalchemy import String, Float
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Cancion(Base):
    __tablename__ = "canciones"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(128))
    minutos: Mapped[int] = mapped_column()
    segundos: Mapped[int] = mapped_column()
    interprete: Mapped[str] = mapped_column(String(128))
    puntajes: Mapped[list[float]] = mapped_column(MutableList.as_mutable(ARRAY(Float)))
