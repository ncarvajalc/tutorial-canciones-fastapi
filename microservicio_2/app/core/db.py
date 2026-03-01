from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from microservicio_2.app.modelos import Base

engine = create_engine("postgresql://estudiante:12345@localhost:5432/tabla")


def init_db():
    Base.metadata.create_all(engine)


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
