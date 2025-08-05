from django.db import models

class Author(models.Model):
    """
    Author Model:
    - Represents an author entity who can write multiple books.
    - Fields:
        name (CharField): Stores the author's name.
    - Relationships:
        One author can be linked to multiple books (One-to-Many relationship).
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book Model:
    - Represents a book entity.
    - Fields:
        title (CharField): The title of the book.
        publication_year (IntegerField): The year the book was published.
        author (ForeignKey): Links each book to a single Author.
    - Relationships:
        Many books can be associated with one author.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
