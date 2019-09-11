from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from pprint import pprint as pp
from .models import Todo
import requests
from decouple import config

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todos/index.html', context)

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due-date')
        Todo.objects.create(title=title, due_date=due_date)
        return redirect('todos:index')
    else:
        return render(request, 'todos/create.html')

def update(request, pk):
    todo = get_object_or_404(Todo, id=pk)

    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due-date')
        todo.title = title
        todo.due_date = due_date
        todo.save()
        return redirect('todos:index')
    else: 
        context = {
            'todo': todo
        }
        return render(request, 'todos/update.html', context)

def delete(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    todo.delete()

    return redirect('todos:index')

@csrf_exempt
def telegram(request):
    print(request.method)
    res = json.loads(request.body)

    text = res.get('message').get('text')
    chat_id = res.get('message').get('chat').get('id')
    base = 'https://api.telegram.org'
    token = config('TOKEN')
    url = f'{base}/bot{token}/sendMessage?text={text}&chat_id={chat_id}'
    requests.get(url)
    return HttpResponse('아무메세지')