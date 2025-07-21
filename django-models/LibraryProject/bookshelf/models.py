from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"


class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class Author(models.Model):
    name = models.CharField(max_length=100)