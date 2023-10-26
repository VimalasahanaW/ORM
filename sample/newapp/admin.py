from django.contrib import admin

# Register your models here.
from .models import Football,FootballAdmin
admin.site.register(Football,FootballAdmin)