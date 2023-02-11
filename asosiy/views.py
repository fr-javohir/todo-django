from django.shortcuts import render, redirect
from .models import *


def home(request):
    if request.method == 'POST':
        sarlavha = request.POST.get('s')
        vaqt = request.POST.get('v')
        batafsil = request.POST.get('b')
        holat = request.POST.get("st")
        Todo.objects.create(sarlavha=sarlavha, vaqt=vaqt,
                            batafsil=batafsil, holat=holat)

        return redirect('/')
    data = {
        "messages": Todo.objects.all()
    }
    return render(request, 'todo.html', data)
