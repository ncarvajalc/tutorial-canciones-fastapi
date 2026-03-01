from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.modelos import Base, Cancion

engine = create_engine("sqlite:///./canciones.db")


def init_db():
    Base.metadata.create_all(engine)


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
