from django.shortcuts import render , get_object_or_404
from .models import Library
from bookshelf.models import Book 
from django.views.generic.detail import DetailView

#function-based view to display all books
def book_list(request):
    books = Book.objects.all()
    return render(request,'relationship_app/list_books.html',{'books': books})

# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    context_object_name = 'library'