from django.db import models
from django.contrib.auth.models import User

class Genres(models.TextChoices):
        FICTION = 'FICT', 'Fiction'
        NF = 'NF', 'Non-Fiction'
        BIO = 'BIO', 'Biography'
        USH ='USH', 'US History'
        WH = 'WH', 'World History'
        PS = 'PS', 'Political Science'
        EDU = 'EDU', 'Education'
        APU = 'AUP', 'Architecture and Urban Planning'

class Author(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.name
     
class Location(models.Model):
     room_name = models.CharField(max_length=50)

     def __str__(self):
          return self.room_name

class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.PositiveSmallIntegerField(max_length=4)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books", default=1)
    genre = models.CharField(max_length=50, choices=Genres.choices, default='NF')
    number_in_collection = models.PositiveSmallIntegerField(default=1)
    picture_url = models.URLField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="location", null=True, blank=True)

    class Meta:
         permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self):
        return self.title

class Event(models.Model):
     title = models.CharField(max_length=100)
     date = models.DateTimeField()
     description = models.TextField()

     def __str__(self):
          return self.title
