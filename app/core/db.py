from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.modelos import Base, Cancion

engine = create_engine("sqlite://")


def init_db():
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        cancion = Cancion(
            titulo="Prueba", minutos=2, segundos=20, interprete="Sultanito"
        )
        session.add(cancion)
        session.commit()
        print(session.query(Cancion).all())
