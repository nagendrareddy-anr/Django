from django.shortcuts import render
from django.http import HttpResponse
from todo_app.models import CreateTask


def index(request):
    tasks = CreateTask.objects.filter(is_completed=False).order_by('-updated_at')
    completed_tasks=CreateTask.objects.filter(is_completed=True)
    return render(request, 'index.html', {'tasks': tasks,'completed_tasks':completed_tasks})
