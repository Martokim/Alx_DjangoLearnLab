from django.db import models

class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # FK to Author
    publication_year = models.IntegerField()
    library = models.ForeignKey(Library, on_delete=models.CASCADE)  # FK to Library

    def __str__(self):
        return f"{self.title} by {self.author.name} ({self.publication_year})"

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)  # One-to-one with Library

    def __str__(self):
        return self.name
