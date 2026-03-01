from celery import Celery

celery_client = Celery(broker="redis://localhost:6379/0")
