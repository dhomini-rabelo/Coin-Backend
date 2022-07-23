from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "COIN.settings")


app = Celery("COIN.celery")
app.config_from_object("django.conf:settings", namespace="CELERY")


CELERY_TASKS = [
]

app.autodiscover_tasks(lambda: CELERY_TASKS)