from django.contrib import admin
from django.urls import path
from asosiy.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view()),
    path('todo/', Home.as_view()),
    path('logout/', LogoutView.as_view()),
    path('register/', Register.as_view()),
    path('del_todo/<int:son>/', Delete_Todo.as_view()),
]
