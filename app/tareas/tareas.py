from datetime import datetime
from app.tareas.celery_app import celery_app
from datetime import timezone


@celery_app.task
def registrar_login(usuario: str):
    fecha = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")
    with open("login.log", "a") as file:
        file.write(f"{usuario} - Inicio de sesión: {fecha}\n")
