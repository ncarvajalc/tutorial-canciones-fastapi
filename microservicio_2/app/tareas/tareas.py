from microservicio_2.app.tareas.celery_app import celery_app
from microservicio_2.app.modelos import Cancion
from microservicio_2.app.core.db import engine
from sqlalchemy.orm import Session


@celery_app.task(name="tabla.registrar_puntaje")
def registrar_puntaje(cancion_json: dict):
    with Session(engine) as db:
        cancion = db.query(Cancion).filter(Cancion.id == cancion_json["id"]).first()
        if not cancion:
            data = cancion_json.copy()
            data.pop("puntaje")
            cancion = Cancion(**data)
            cancion.puntajes = [cancion_json["puntaje"]]
            db.add(cancion)
        else:
            cancion.puntajes.append(cancion_json["puntaje"])
            db.add(cancion)
        db.commit()
