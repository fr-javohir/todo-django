from django.shortcuts import render
from .models import *

def home(request):
    return render(request,'todo.html')
# Create your views here.
