from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from .utils import searchTask

@login_required(login_url='login')
def tasks(request):
    incomplete_task_count =  Task.objects.filter(user=request.user).filter(completed=False).count()
    tasks, search_query = searchTask(request)
    tasks = tasks.filter(user=request.user)
    context = {
        'search_query':search_query,
        'tasks': tasks,
        'incomplete_task_count':incomplete_task_count,
    }
    return render(request, 'tasks/tasks.html', context)

@login_required(login_url='login')
def task(request, pk):
    task = Task.objects.get(id=pk)
    context = {
        'task': task
    }
    return render(request, 'tasks/task.html', context)



@login_required(login_url='login')
def taskCreate(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.user=request.user
            task.save()
            return redirect('tasks')
    context = {
        'form': form
    }
    return render(request, 'tasks/task-form.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def taskDelete(request, pk):
    task =Task.objects.get(id=pk)
    context ={
        'task': task
    }
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    
    return render(request, 'tasks/task-delete-confirm.html',context)


@login_required(login_url='login')
def completeTask(request, pk):
    try:
        task = Task.objects.get(id=pk)
        task.completed = True
        task.save()
    except Task.DoesNotExist:
        # Handle the case when the task does not exist
        pass

    return redirect('task', pk=pk)



@login_required(login_url='login')
def incompleteTask(request, pk):
    try:
        task = Task.objects.get(id=pk)
        task.completed = False
        task.save()
    except Task.DoesNotExist:
        # Handle the case when the task does not exist
        pass

    return redirect('task', pk=pk)