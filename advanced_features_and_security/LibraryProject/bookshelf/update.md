# Update Book

```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Print updated book
print(book)
```

**Expected Output:**

```
Nineteen Eighty-Four by George Orwell (1949)
```
