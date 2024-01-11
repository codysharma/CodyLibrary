from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.PositiveSmallIntegerField(max_length=4)
    number_in_collection = models.PositiveSmallIntegerField(default=1)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books", default=1)

    def __str__(self):
        return self.title