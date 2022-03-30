import rest_framework.permissions
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from quickstart.tasks import count_users
from snippets.tasks import debug_task


# Create your views here.

class CeleryAppViewSet(viewsets.GenericViewSet):
    permission_classes = [rest_framework.permissions.AllowAny, ]

    @action(detail=False)
    def debug(self, request, *args, **kwargs):
        result = debug_task.delay()
        return HttpResponse(result)

    @action(detail=False)
    def count(self, request, *args, **kwargs):
        result = count_users.delay()

        return HttpResponse(result)
