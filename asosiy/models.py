from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Talaba(models.Model):
    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)
    tb_raqam = models.CharField(max_length=8)
    kurs = models.PositiveSmallIntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return Talaba.ism


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
    talaba = models.ForeignKey(
        Talaba, on_delete=models.SET_NULL, null=True)
