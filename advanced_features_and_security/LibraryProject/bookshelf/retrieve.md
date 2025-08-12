# Retrieve Book

```python
from bookshelf.models import Book

# Retrieve all books
books = Book.objects.all()
for b in books:
    print(b.title, b.author, b.publication_year)
```

**Expected Output:**

```
1984 George Orwell 1949
```

Or retrieving a single book:

```python
book = Book.objects.get(title="1984")
print(book.title)
print(book.author)
print(book.publication_year)
```

**Expected Output:**

```
1984
George Orwell
1949
```
