from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import CreateTask


def add_task(request):
    tasks = request.POST['task']
    CreateTask.objects.create(task=tasks)
    return redirect('index')


def mark_done(request, pk):
    task = get_object_or_404(CreateTask, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('index')


def mark_undone(request, pk):
    task = get_object_or_404(CreateTask, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('index')


def edit_task(request,pk):
    get_task=get_object_or_404(CreateTask,pk=pk)
    if request.method == 'POST':
        new_task=request.POST['task']
        get_task.task=new_task
        get_task.save()
        return redirect('index')
    else:
        context={
            'get_task':get_task
        }
    return render(request,'edit.html',context)


def delete_task(request,pk):
    task = get_object_or_404(CreateTask, pk=pk)
    task.delete()
    return redirect('index')
