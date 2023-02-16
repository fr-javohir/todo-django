from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.views import View


class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                "messages": Todo.objects.filter(talaba__user=request.user)
            }
            return render(request, 'todo.html', data)
        return redirect('/')

    def post(self, request):
        sarlavha = request.POST.get('s')
        vaqt = request.POST.get('v')
        batafsil = request.POST.get('b')
        holat = request.POST.get("st")
        talaba = Talaba.objects.get(user=request.user)
        Todo.objects.create(sarlavha=sarlavha, vaqt=vaqt,
                            batafsil=batafsil, holat=holat, talaba=talaba)
        return redirect('/todo')


class Delete_Todo(View):
    def get(self, request, son):
        dt = Todo.objects.get(id=son)
        if dt.talaba.user == request.user:
            # pl.talaba = Talaba.objects.get(user = request.user)
            dt.delete()
        return redirect('/todo')


class LoginView(View):
    def post(self, request):
        user = authenticate(username=request.POST.get("l"),
                            password=request.POST.get("p"))
        if user is None:
            return redirect('/')
        login(request, user)
        return redirect('/todo/')

    def get(self, request):
        return render(request, 'login.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class Register(View):
    def post(self, request):
        if request.POST.get('p') == request.POST.get('cp'):
            user = User.objects.create_user(
                username=request.POST.get('l'),
                password=request.POST.get('p')
            )
            ism_f = request.POST.get("i")
            Talaba.objects.create(
                ism=ism_f[:ism_f.find(" ")],
                familiya=ism_f[ism_f.find(" ")+1:],
                tb_raqam=request.POST.get("tr"),
                kurs=request.POST.get("k"),
                user=user
            )
            return redirect('/')

    def get(self, request):
        return render(request, 'register.html')
