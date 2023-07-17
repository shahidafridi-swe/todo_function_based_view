from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import CustomUserCreationForm


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('tasks')

    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('tasks')

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)


def loginUser(request):

    if request.user.is_authenticated:
        return redirect('tasks')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)

        except User.DoesNotExist:
            messages.error(request, "User doesn't exit!!!")
            return redirect('login')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('tasks')
        else:
            messages.error(request, 'Password is incorrect')
            return redirect('login')

    return render(request, 'users/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')