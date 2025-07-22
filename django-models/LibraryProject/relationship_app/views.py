from django.shortcuts import render , get_object_or_404
from .models import Library
from bookshelf.models import Book 
from django.views.generic.detail import DetailView

# Import necessary modules for authentication
from django.contrib.auth import login
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# import necessary models and user model
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test




#function-based view to display all books
def list_books(request):
    books = Book.objects.all()
    return render(request,'relationship_app/list_books.html',{'books': books})

# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    context_object_name = 'library'

# user registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Automatically log in the user after registration
            return redirect('list_books')  
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# user login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books') 
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})


# user logout view
def logout_view(request):
    logout(request)
    return redirect('login')  

# user model to include user roles permission
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('librarian', 'Librarian'),
        ('member', 'Member'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
    def __str__(self):
        return f"{self.user.username} - {self.role}"

# role-based views 
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html') 
