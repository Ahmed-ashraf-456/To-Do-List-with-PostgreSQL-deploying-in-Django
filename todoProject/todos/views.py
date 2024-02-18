from django.shortcuts import render,redirect
from .models import Todo 
from django.http import HttpRequest
# Create your views here.

def index (request):
    context = { 'todo_list': Todo.objects.all()}
    return render (request , 'todos/index.html', context)

def insert_todo_item (request : HttpRequest):
    todo = Todo(content = request.POST['content'])
    todo.save()
    return redirect ('/')

def delete_todo_item (request , todo_id):
    print (todo_id)
    todo_to_delete = Todo.objects.get(id= todo_id)
    todo_to_delete.delete()
    return redirect('/')