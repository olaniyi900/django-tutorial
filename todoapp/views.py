from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Todo


class TodoListView(ListView):
    model = Todo


class TodoCreateView(CreateView):
    model = Todo
    success_url = '/todoapp/'
    template_name = 'todoapp/todo_list.html'
    fields = ['text']

    def get_queryset(self):
        return Todo.objects.all()
    


