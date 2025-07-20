from django.shortcuts import render
from bookshelf.models import Book 
from django.views.generic.detail import DetailView
from bookshelf.models import Library 

#function-based view to display all books
def book_list(request):
    books = Book.objects.all()
    return render(request,'list_books.html',{'books': books})