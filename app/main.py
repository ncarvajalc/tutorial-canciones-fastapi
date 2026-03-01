from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.core.db import init_db
from app.rutas.canciones import router as canciones_router
from app.rutas.signin import router as signin_router
from app.rutas.albumes import router as albumes_router
from app.rutas.album_usuario import router as album_usuario_router
from app.rutas.album_canciones import router as album_canciones_router
from app.rutas.login import router as login_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Tutorial Canciones FastAPI", root_path="/proxy/8000", lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(canciones_router)
app.include_router(signin_router)
app.include_router(albumes_router)
app.include_router(album_usuario_router)
app.include_router(album_canciones_router)
app.include_router(login_router)
