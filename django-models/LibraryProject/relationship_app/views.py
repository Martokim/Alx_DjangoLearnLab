from django.shortcuts import render , get_object_or_404
from .models import Library
from bookshelf.models import Book 
from django.views.generic.detail import DetailView

# Import necessary modules for authentication
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


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
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('book-list')  # redirect to home or book list
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# user login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book-list')  # or wherever you want
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# user logout view
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')
