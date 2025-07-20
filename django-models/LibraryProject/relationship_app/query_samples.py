'''
 Query all books by a specific author.
 List all books in a library.
 Retrieve the librarian for a library.
'''
from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return author.books.all()
    except Author.DoesNotExist:
        return None 

def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return None

def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian  # Corrected from .librarians.all()
    except Library.DoesNotExist:
        return None
    except Librarian.DoesNotExist:
        return None
