from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Todo(models.Model):
    status = [
        ("bajarildi", "bajarildi"),
        ("bajarilmoqda", "bajarilmoqda"),
        ("bajarilmadi", "bajarilmadi"),

    ]
    sarlavha = models.CharField(max_length=70)
    vaqt = models.DateField()
    batafsil = models.TextField()
    holat = models.CharField(max_length=20, choices=status)
    foydalanuvchi = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
