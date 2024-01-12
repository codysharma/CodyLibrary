from django.contrib import admin
from .models import Author, Book, Event

# Register your models here.
admin.site.register([Book, Author, Event])
