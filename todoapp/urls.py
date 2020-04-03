from django.urls import path
from . import views


urlpatterns = [
    path('', views.TodoListView.as_view(), name='todo'),
    path('', views.TodoCreateView.as_view(), name='todo_new'),
]
