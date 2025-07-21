from django.db import models

# 1. Author model
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 2. Book model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)  
    publication_year = models.IntegerField()


    def __str__(self):
        return f"{self.title} by {self.author.name}"

# 3. Library model
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(
        Book,  # Book is already defined above
        related_name='libraries'
    )

    def __str__(self):
        return self.name

# 4. Librarian model with OneToOne relation
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(
        Library,
        on_delete=models.CASCADE,
        related_name='librarian'
    )

    def __str__(self):
        return f"{self.name} (Librarian of {self.library.name})"
