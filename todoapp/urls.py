from django.urls import path
from . import views


urlpatterns = [
    path('', views.TodoListView.as_view(), name='todo'),
    path('new/', views.TodoCreateView.as_view(), name='todo_new'),
]
