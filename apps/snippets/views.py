from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewSet automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewSet automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # 可以通过不同的renderer_classes返回不同的Content-Type
    # https://www.django-rest-framework.org/api-guide/renderers/#third-party-packages
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    # https://stackoverflow.com/questions/52551257/django-detailview-get-queryset-and-get-object
    # https://www.django-rest-framework.org/api-guide/viewsets/#introspecting-viewset-actions
    # https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/#refactoring-to-use-viewsets

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)  # https://www.django-rest-framework.org/api-guide/serializers/#saving-instances
