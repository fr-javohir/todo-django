from django.shortcuts import render
from .models import *


def home(request):
    data = {
        "messages": Todo.objects.all()
    }
    return render(request, 'todo.html', data)
# Create your views here.
