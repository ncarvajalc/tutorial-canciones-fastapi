from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from microservicio_2.app.core.db import init_db
from microservicio_2.app.rutas.canciones import router as canciones_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Microservicio 2 - Tabla de Puntajes",
    root_path="/proxy/8002",
    lifespan=lifespan,
)

app.include_router(canciones_router)
