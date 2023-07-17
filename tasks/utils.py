from django.db.models import Q 
from .models import Task

def searchTask(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    tasks = Task.objects.filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query)
    )

    return tasks, search_query