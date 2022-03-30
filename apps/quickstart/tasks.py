# Create your tasks here

from celery import shared_task
from django.contrib.auth.models import User


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def count_users():
    return User.objects.count()


@shared_task
def rename_user(user_id, name):
    w = User.objects.get(id=user_id)
    w.name = name
    w.save()
