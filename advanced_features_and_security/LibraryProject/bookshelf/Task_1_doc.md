#  Django Permissions and Groups Setup – LibraryProject

This guide explains how custom permissions and user groups are set up and used in the `LibraryProject`, specifically for managing `Book` objects within the `bookshelf` app.

---

##  Custom Permissions

Custom permissions are defined inside the `Meta` class of the `Book` model.

###  Defined Permissions:
```python
class Book(models.Model):
    ...
    class Meta:
        permissions = [
            ("can_create", "Can create books"),
            ("can_edit", "Can edit books"),
            ("can_delete", "Can delete books"),
        ]
