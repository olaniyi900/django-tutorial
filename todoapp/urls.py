from django.urls import path
from . import views


urlpatterns = [
    path('', views.TodoListView.as_view(), name='todo'),
    path('new/', views.todoCreate, name='todo_create'),
    path('<int:todo_id>/delete/', views.todoDelete, name='todo_delete'),
    path('<int:id>/update/', views.todoDelete, name='todo_update'),
    #path('new/', views.TodoCreateView.as_view(), name='todo_new'),
]
