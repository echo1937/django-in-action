from rest_framework.routers import DefaultRouter

from .views import CeleryAppViewSet

router = DefaultRouter()
router.register(r'celery', CeleryAppViewSet, basename='celery')
