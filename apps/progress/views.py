# Create your views here.
from django.shortcuts import render

from .tasks import my_task


def display_progress(request):
    result = my_task.delay(30)
    return render(request, 'display_progress.html', {'task_id': result.task_id})
