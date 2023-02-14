from django.contrib import admin
from django.urls import path
from asosiy.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', home),
    path('', loginview),
    path('logout/', logoutview),
]
