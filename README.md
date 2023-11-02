# Ex02 Django ORM Web Application
## Date:18-10-2023 

## AIM
To develop a Django application to store and retrieve data from a Football Players database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create 10 Football players

## PROGRAM

```
admin.py
from django.contrib import admin

# Register your models here.
from .models import Football,FootballAdmin
admin.site.register(Football,FootballAdmin)
models.py
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
    
```
## OUTPUT

![Alt text](<Screenshot 2023-11-01 094756.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
from django.contrib import admin


    


