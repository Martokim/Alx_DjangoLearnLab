from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book 
from .serializers import BookSerializer


# Create your views here.

# 1.list all books
class BookListView(generics.ListAPIView):
    """
  API view to list all books with filtering, searching, and ordering capabilities.
    - Filtering: Filter books by title, author, or publication year.
    - Searching: Search books by title or author's name.
    - Ordering: Order books by title or publication year.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]# unauthenticated users can read, but cannot perform CRUD operations
   # Enable filtering , searchin and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Define filter fields
    filterset_fields = ['title', 'author_name','publication_year']
    
    # Define search fields
    search_fields = ['title', 'author_name']

    # Define ordering fields
    ordering_fields = ['title', 'publication_year']

    # Define default ordering
    ordering = ['title']

# 2. Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """
    BookDetailView:
    - Retrieves a single book by its ID.
    - Accessible by anyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # unauthenticated users can read, but cannot perform CRUD operations

# 3. create a new book (create)
class BookCreateView(generics.CreateAPIView):
    """
    BookCreateView:
    - Allows creation of a new book.
    - Accessible by authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create books

# 4. Update an existing book (update)
class BookUpdateView(generics.UpdateAPIView):
    """
    BookUpdateView:
    - Allows updating an existing book by its ID.
    - Accessible by authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Only authenticated users can update books

# 5. Delete a book (delete))
class BookDeleteView(generics.DestroyAPIView):
    """
    BookDeleteView:
    - Allows deletion of a book by its ID.
    - Accessible by authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]# Only authenticated users can delete books
