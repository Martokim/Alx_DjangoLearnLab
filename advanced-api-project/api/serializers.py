from rest_framework import serializers
from .models import Book, Author
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer:
    - Serializes the Book model.
    - Includes a validation to ensure publication_year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year']


class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer:
    - Serializes the Author model.
    - Includes nested serialization of all related books using BookSerializer.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']


class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer:
    - Serializes the Book model with nested Author info.
    """
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
        read_only_fields = ['author']

    def validate_publication_year(self, value):
        """
        Custom Validator:
        Ensures the publication year is not in the future.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
