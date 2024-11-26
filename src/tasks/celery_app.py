from celery import Celery
from celery.schedules import crontab

from src.config import settings

celery = Celery(
    "tasks",
    broker=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
)


celery.conf.beat_schedule = {
    "everyday-task": {
        "task": "src.tasks.tasks.get_file_from_site",
        "schedule": crontab(hour="10", minute="0"),
    }
}
celery.autodiscover_tasks()
