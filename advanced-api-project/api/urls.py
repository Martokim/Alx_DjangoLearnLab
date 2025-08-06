from django.urls import path, include
from .views import (
    BookListCreateView,
    BookRetrieveUpdateDeleteView,
    AuthorListCreateView,
    AuthorRetrieveUpdateDeleteView,
)

urlpatterns = [
    
    # BOOK ENDPOINTS    
    path('books/', BookListCreateView.as_view(), name='book-list-create'),  
    # GET → List all books
    # POST → Create a new book

    path('books/<int:pk>/', BookRetrieveUpdateDeleteView.as_view(), name='book-detail'),  
    # GET → Retrieve a book by ID
    # PUT/PATCH → Update book
    # DELETE → Delete book

   
    # AUTHOR ENDPOINTS
     path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),  
    # GET → List all authors
    # POST → Create new author

    path('authors/<int:pk>/', AuthorRetrieveUpdateDeleteView.as_view(), name='author-detail'),  
    # GET → Retrieve author details by ID
    # PUT/PATCH → Update author
    # DELETE → Delete author   
]
