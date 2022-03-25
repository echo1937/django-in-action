from rest_framework import routers

from quickstart.views import UserViewSet, GroupViewSet

# Wire up our API using automatic URL routing.
quickstart = routers.DefaultRouter()
quickstart.register(r'users', UserViewSet)
quickstart.register(r'groups', GroupViewSet)
