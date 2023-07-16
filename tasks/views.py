from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def tasks(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks/tasks.html', context)


def task(request, pk):
    task = Task.objects.get(id=pk)
    context = {
        'task': task
    }
    return render(request, 'tasks/task.html', context)

def taskCreate(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    context = {
        'form': form
    }
    return render(request, 'tasks/task-form.html', context)

def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('tasks')
    context = {
        'form': form
    }
    return render(request, 'tasks/task-form.html', context)