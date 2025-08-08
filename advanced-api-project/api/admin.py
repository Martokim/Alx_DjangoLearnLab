from django.contrib import admin
from .models import Book, Author

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author__name')
    list_filter = ('publication_year',)
    ordering = ('title',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'Book_title')
    ordering = ('name',)