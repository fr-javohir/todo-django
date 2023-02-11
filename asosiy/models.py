from django.db import models

# Create your models here.


class Todo(models.Model):
    status = [
        ("bajarildi","bajarildi"),
        ("bajarilmoqda","bajarilmoqda"),
        ("bajarilmadi","bajarilmadi"),
        
    ]     
    sarlavha = models.CharField(max_length=70)
    vaqt = models.DateField()
    batafsil = models.TextField()
    holat = models.CharField(max_length=20,choices=status)
