import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_in_action.settings')
app = Celery('django_in_action')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()
