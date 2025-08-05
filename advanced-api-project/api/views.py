from django.shortcuts import render
from rest_framework import generics , permissions
from .models import Author, Book 
from .serializers import AuthorSerializer , BookSerializer


# Create your views here.

# 1.list all books
class BookListView(generics.ListAPIView):
    """
    BookListView:
    - Retrieves a list of all books.
    - Accessible by anyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny] # Allow any user to access this view

# 2. Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """
    BookDetailView:
    - Retrieves a single book by its ID.
    - Accessible by anyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# 3. create a new book (create)
class BookCreateView(generics.CreateAPIView):
    """
    BookCreateView:
    - Allows creation of a new book.
    - Accessible by authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create books

# 4. Update an existing book (update)
class BookUpdateView(generics.UpdateAPIView):
    """
    BookUpdateView:
    - Allows updating an existing book by its ID.
    - Accessible by authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# 5. Delete a book (delete))
class BookDeleteView(generics.DestroyAPIView):
    """
    BookDeleteView:
    - Allows deletion of a book by its ID.
    - Accessible by authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
