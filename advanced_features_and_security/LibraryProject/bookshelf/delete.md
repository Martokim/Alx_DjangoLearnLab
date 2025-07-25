```python
from bookshelf.models import Book

# Retrieve the book instance you want to delete
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Check if the book was deleted
Book.objects.all()
