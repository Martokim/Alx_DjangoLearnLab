from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    AuthorListView,
    AuthorDetailView,
    AuthorCreateView,
    AuthorUpdateView,
    AuthorDeleteView,
)

urlpatterns = [
    # BOOK ENDPOINTS
    path('books/', BookListView.as_view(), name='book-list'),  
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  
    path('books/create', BookCreateView.as_view(), name='book-create'),  
    path('books/update/<int:pk>', BookUpdateView.as_view(), name='book-update'),  
    path('books/delete/<int:pk>', BookDeleteView.as_view(), name='book-delete'),  

    # AUTHOR ENDPOINTS
    path('authors/', AuthorListView.as_view(), name='author-list'),  
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),  
    path('authors/create', AuthorCreateView.as_view(), name='author-create'),  
    path('authors/update/<int:pk>', AuthorUpdateView.as_view(), name='author-update'),  
    path('authors/delete/<int:pk>', AuthorDeleteView.as_view(), name='author-delete'),  
]
