from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *


def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            sarlavha = request.POST.get('s')
            vaqt = request.POST.get('v')
            batafsil = request.POST.get('b')
            holat = request.POST.get("st")
            Todo.objects.create(sarlavha=sarlavha, vaqt=vaqt,
                                batafsil=batafsil, holat=holat, foydalanuvchi=request.user)

            return redirect('/todo')
        data = {
            "messages": Todo.objects.filter(foydalanuvchi=request.user)
        }
        return render(request, 'todo.html', data)
    return redirect('/')


def loginview(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get("l"),
                            password=request.POST.get("p"))
        if user is None:
            return redirect('/')
        login(request, user)
        return redirect('/todo/')
    return render(request, 'login.html')


def logoutview(request):
    logout(request)
    return redirect('/')
