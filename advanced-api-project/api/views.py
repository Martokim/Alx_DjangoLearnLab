from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


# BOOK VIEWS
class BookListCreateView(generics.ListCreateAPIView):
    """
    GET → List all books (supports filtering, searching, and ordering)
    POST → Create a new book (authenticated users only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # <-- Changed from AllowAny

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']


class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET → Retrieve book by ID
    PUT/PATCH/DELETE → Authenticated users only
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # <-- Changed from AllowAny


# AUTHOR VIEWS
class AuthorListCreateView(generics.ListCreateAPIView):
    """
    GET → List all authors
    POST → Create a new author (authenticated users only)
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # <-- Changed from AllowAny


class AuthorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET → Retrieve author details
    PUT/PATCH/DELETE → Authenticated users only
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # <-- Changed from AllowAny
