from django.contrib import admin
from .models import Author, Book, Event, Location, ReadingList, Contact

# Register your models here.
admin.site.register([Book, Author, Event, Location, ReadingList, Contact])
