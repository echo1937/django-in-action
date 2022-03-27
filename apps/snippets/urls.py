from django.urls import path, include
from rest_framework.routers import DefaultRouter

from snippets import views

# Create a router and register our viewSets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename="snippet")
router.register(r'users', views.UserViewSet, basename="user")
# 官网页面的手册basename是snippets和users，结果排错排一晚上

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
