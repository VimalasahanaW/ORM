from django.db import models
from django.contrib import admin
# Create your models here.
class Football (models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    country=models.CharField(max_length=20)
    no_of_awards=models.IntegerField()
    email=models.EmailField()

class FootballAdmin(admin.ModelAdmin):
    list_display=('name','age','country','no_of_awards','email')
    

