from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)
from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

# URL routing for CRUD operations on Book model:
# - ListView: /books/ - List all books.
# - DetailView: /books/<int:pk>/ - Retrieve a single book by ID.
# - CreateView: /books/create/ - Create a new book (Authenticated users only).
# - UpdateView: /books/update/<int:pk>/ - Update a book (Authenticated users only).
# - DeleteView: /books/delete/<int:pk>/ - Delete a book (Authenticated users only).

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]


urlpatterns = [
    path('books/',BookListView.as_view(), name='book-list'), # list all books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),# get a book by ID
    path('books/create/', BookCreateView.as_view(), name='book-create'), # create a new book
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'), 
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
    ]