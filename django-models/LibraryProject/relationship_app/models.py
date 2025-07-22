from django.db import models
from django.contrib.auth.models import User

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

# 5.UserProfile model to include user roles
# user model to include user roles permission
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('librarian', 'Librarian'),
        ('member', 'Member'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
    def __str__(self):
        return f"{self.user.username} - {self.role}"