from django.urls import path
import relationship_app.views as views
from django.contrib.auth.views import LoginView, LogoutView

from .views import (
    list_books,
    LibraryDetailView,
    register,
    login_view,
    admin_view,
    librarian_view,
    member_view,
    logout_view,
    add_book,
    edit_book,
    delete_book
)

urlpatterns = [
    path('books/', views.list_books, name='book-list'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),

    # Auth views
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Role-based access views
    path('admin-area/', admin_view, name='admin-view'),
    path('librarian-area/', librarian_view, name='librarian-view'),
    path('member-area/', member_view, name='member-view'),

     # Book management
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', delete_book, name='delete-book'),

    
]



