---

##  Project Structure
LibraryProject/
├── bookshelf/
│ ├── forms.py 
│ ├── models.py 
│ ├── views.py 
│ ├── urls.py
│ ├── templates/
│ │ └── bookshelf/
│ │ ├── book_list.html
│ │ └── form_example.html
│ └── admin.py
├── LibraryProject/
│ └── settings.py 


---

##  Custom User Model

A custom user model `CustomUser` extends `AbstractUser`, with:

- `date_of_birth` (DateField)
- `profile_photo` (ImageField)

Defined in `bookshelf/models.py`, and set via:
```python
# LibraryProject/settings.py
AUTH_USER_MODEL = 'bookshelf.CustomUser'

```
## Book Model and permissions
permissions = [
    ("can_create", "Can create a book"),
    ("can_edit", "Can edit a book"),
    ("can_view", "Can view a book"),
    ("can_delete", "Can delete a book"),
]


## Security Settings
``` python 
# LibraryProject/settings.py
  X_FRAME_OPTIONS = 'DENY'
  CSRF_COOKIE_SECURE = True

```

## Testing permissions (via Django shell)
```Python
  from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model
User = get_user_model()
user = User.objects.get(username='username')

# Grant view permission
view_perm = Permission.objects.get(codename='can_view')
user.user_permissions.add(view_perm)

```

