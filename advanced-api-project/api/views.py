from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework  
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


# BOOK VIEWS


class BookListCreateView(generics.ListCreateAPIView):
    """
    API Endpoint: /api/books/
    - GET: List all books (supports filtering, searching, and ordering).
    - POST: Create a new book (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Unauthenticated users can read only

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']  # Filter by these fields
    search_fields = ['title', 'author__name']  # Search by book title or author's name
    ordering_fields = ['title', 'publication_year']  # Order results by title or year
    ordering = ['title']  # Default ordering by title

class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    API Endpoint: /api/books/<id>/
    - GET: Retrieve a single book by ID.
    - PUT/PATCH: Update a book (authenticated users only).
    - DELETE: Delete a book (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can modify


# AUTHOR VIEWS

class AuthorListCreateView(generics.ListCreateAPIView):
    """
    API Endpoint: /api/authors/
    - GET: List all authors (includes their related books).
    - POST: Create a new author (authenticated users only).
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read for all, create for authenticated

class AuthorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    API Endpoint: /api/authors/<id>/
    - GET: Retrieve a single author and their books.
    - PUT/PATCH: Update author details (authenticated users only).
    - DELETE: Delete an author (authenticated users only).
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
