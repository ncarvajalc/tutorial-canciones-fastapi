from datetime import datetime, timezone
from tareas.celery_app import celery_app


@celery_app.task(name="tareas.registrar_login")
def registrar_login(usuario: str):
    fecha = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")
    with open("login.log", "a") as file:
        file.write(f"{usuario} - Inicio de sesión: {fecha}\n")
