import httpx
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(title="Microservicio 1 - Puntaje Canciones", root_path="/proxy/8001")

CANCIONES_APP_URL = "http://localhost:8000"


class PuntajeSchema(BaseModel):
    puntaje: float


@app.post("/canciones/{cancion_id}/puntaje")
def agregar_puntaje(cancion_id: int, puntaje: PuntajeSchema):
    response = httpx.get(f"{CANCIONES_APP_URL}/canciones/{cancion_id}")

    if response.status_code == 404:
        return JSONResponse(status_code=404, content=response.json())

    cancion = response.json()
    cancion["puntaje"] = puntaje.puntaje
    return cancion
