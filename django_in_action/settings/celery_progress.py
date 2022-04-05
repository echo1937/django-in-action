from .settings import INSTALLED_APPS

INSTALLED_APPS += [
    'django_celery_results',
    'celery_progress'
]

CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'
CELERY_ACCEPT_CONTENT = ['json']  # Default: {'json'} (set, list, or tuple).
CELERY_TASK_SERIALIZER = 'json'  # Default: "json" (since 4.0, earlier: pickle).
