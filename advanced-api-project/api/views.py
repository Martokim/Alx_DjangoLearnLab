from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book 
from .serializers import BookSerializer


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
    permission_classes = [IsAuthenticatedOrReadOnly]# unauthenticated users can read, but cannot perform CRUD operations

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
