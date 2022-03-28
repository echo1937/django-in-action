# Serializers define the API representation.
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
        extra_kwargs = {
            'url': {'view_name': 'other-detail', 'lookup_field': 'pk'}
        }
        ref_name = 'quickstart_user'
        # https://drf-spectacular.readthedocs.io/en/latest/drf_yasg.html#compatibility

    # https://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer
    # https://stackoverflow.com/questions/66034534/how-can-i-change-hyperlinkedmodelserializers-default-pk-lookup-url-kwarg


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
