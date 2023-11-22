# First steps with Django
# https://docs.celeryproject.org/en/latest/django/first-steps-with-django.html

from __future__ import absolute_import
import datetime
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
# from apps.students.tasks import status
# from apps.students.models import studentList

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery(
    broker=settings.CELERY_BROKER_URL, backend=settings.CELERY_RESULT_BACKEND
)
app.config_from_object("django.conf:settings")
app.autodiscover_tasks(settings.INSTALLED_APPS)

if __name__ == "__main__":
    app.start()

@app.task
def helloWord():
  print('hello Word in Celery')