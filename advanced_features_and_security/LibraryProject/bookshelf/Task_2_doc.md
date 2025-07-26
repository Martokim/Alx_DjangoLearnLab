# LibraryProject – Task 2: Access and Permissions

This project implements a basic Library Management System using Django, with a focus on **role-based access control**, **form handling**, and **secure book management**.

---

##  Objectives

- Introduce custom user model with additional fields.
- Implement access control using Django’s permission system.
- Securely manage book creation and listing via forms.
- Follow ALX best practices for modular, secure web applications.

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

