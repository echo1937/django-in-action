"""django_in_action URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import routers

from quickstart.urls import router as quickstart_router
from snippets.urls import router as snippets_router

router = routers.DefaultRouter()
router.registry.extend(quickstart_router.registry)
router.registry.extend(snippets_router.registry)
# https://blog.csdn.net/weixin_43689950/article/details/115915788

urlpatterns = [
    path('admin/', admin.site.urls),  # admin
    path('api-auth/', include('rest_framework.urls')),  # rest_framework
    path('', include(router.urls)),
    # path('', include(quickstart.urls)),
    # path('', include('snippets.urls')),
    # ------------ simple JWT ------------
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
]

# https://drf-spectacular.readthedocs.io/en/latest/readme.html#take-it-for-a-spin
urlpatterns += [
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

# progress模块的路径
from progress.views import display_progress

urlpatterns += [
    path('display_progress/', display_progress, name='display_progress'),
    path('celery-progress/', include('celery_progress.urls'))
]
