from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style']
        # explicitly set the view_name and lookup_field options in the extra_kwargs
        extra_kwargs = {
            'url': {'view_name': 'snippet-detail', 'lookup_field': 'pk'}
        }

    # https://www.django-rest-framework.org/api-guide/fields/#source
    # https://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer
    # https://stackoverflow.com/questions/66034534/how-can-i-change-hyperlinkedmodelserializers-default-pk-lookup-url-kwarg


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
