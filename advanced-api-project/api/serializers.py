from rest_framework import serializers
from .models import Book, Author
from datetime import date

class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer:
    - Serializes the Author model.
    - Fields:
        id: Automatically generated primary key.
        name: Name of the author.
    - Relationship Handling:
        Books written by this author will be serialized separately using BookSerializer (nested serialization).
    """
    class Meta:
        model = Author
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer:
    - Serializes the Book model.
    - Fields:
        id: Automatically generated primary key.
        title: Title of the book.
        publication_year: Year the book was published.
        author: Nested serialization of the related Author object (read-only).
    - Custom Validation:
        Ensures that 'publication_year' is not set in the future.
    """
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
        read_only_fields = ['author']

    def validate_publication_year(self, value):
        """
        Custom Validator:
        - Ensures the publication year is not in the future.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
