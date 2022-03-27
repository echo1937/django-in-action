from rest_framework import routers

from quickstart.views import UserViewSet, GroupViewSet

# Wire up our API using automatic URL routing.
router = routers.DefaultRouter()
router.register(r'quickstart-users', UserViewSet, basename='other')
router.register(r'groups', GroupViewSet)

# https://www.django-rest-framework.org/api-guide/routers/#usage
