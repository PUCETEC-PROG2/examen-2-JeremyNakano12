from django.contrib import admin
from .models import Movies
# Register your models here.

@admin.register(Movies)
class Moviesadmin(admin.ModelAdmin):
    pass