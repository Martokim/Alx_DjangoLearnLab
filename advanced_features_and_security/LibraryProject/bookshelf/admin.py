from django.contrib import admin
from .models import Book

@admin.register(Book) # only those with admin privileges can access this model in the admin interface
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')
