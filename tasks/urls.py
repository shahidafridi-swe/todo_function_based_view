from django.urls import path
from . import views


urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('task/<str:pk>', views.task, name='task'),
    path('task-create/', views.taskCreate, name='task-create'),
]
