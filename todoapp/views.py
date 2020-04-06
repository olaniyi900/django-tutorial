from django.shortcuts import render, redirect
from django.views.generic import ListView
# from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import TodoForm
from .models import Todo


class TodoListView(ListView):
    model = Todo




def todoCreate(request):
    qs = Todo.objects.all()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo_text = form.cleaned_data['text']
            todo = Todo()
            todo.text = todo_text
            todo.save()
            return redirect('todo_create')
    else:
        form = TodoForm()
    return render(request, 'todoapp/todo_list.html', {'todo_list':qs, 'form':form})
    
    

def todoUpdate(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            Todo(**form.cleaned_data)
            todo.save()
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todoapp/todo_list.html', {'form':form})    
    


def todoDelete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo_create') #render(request, 'todoapp/todo_list.html', {'todo':todo})






# class TodoCreateView(CreateView):
#     model = Todo
#     success_url = '/todoapp/'
#     template_name = 'todoapp/todo_list.html'
#     fields = ['text']

#     def get_queryset(self):
#         return Todo.objects.all()
    


