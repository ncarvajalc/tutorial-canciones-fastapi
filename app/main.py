from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from app.core.db import init_db
from app.rutas.canciones import router as canciones_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Tutorial Canciones FastAPI", root_path="/proxy/8000", lifespan=lifespan
)

app.include_router(canciones_router)