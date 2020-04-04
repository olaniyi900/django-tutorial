from django.shortcuts import render, redirect
from django.views.generic import ListView
# from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Todo


class TodoListView(ListView):
    model = Todo




def todoCreate(request):
    qs = Todo.objects.all()
    todo_item = request.POST['todo']
    Todo.objects.create(text=todo_item)
    return render(request, 'todoapp/todo_list.html', {'todo_list':qs})


# def todoDelete(request, todo_id):
#     todo_item = Todo.objects.get(id=todo_id)
#     todo_item.delete()
#     return redirct('todo_create')



# class TodoCreateView(CreateView):
#     model = Todo
#     success_url = '/todoapp/'
#     template_name = 'todoapp/todo_list.html'
#     fields = ['text']

#     def get_queryset(self):
#         return Todo.objects.all()
    


