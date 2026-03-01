from celery import Celery

celery_app = Celery(
    "tutorial_canciones",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)
