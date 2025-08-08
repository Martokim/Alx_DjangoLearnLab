from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from api.models import Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create test user & log in
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')

        # Create sample books
        self.book1 = Book.objects.create(
            title="Book One",
            author="Author A",
            publication_year=2000
        )
        self.book2 = Book.objects.create(
            title="Book Two",
            author="Author B",
            publication_year=2010
        )

        # URLs from your urls.py
        self.list_url = reverse('book-list-create')
        self.detail_url = reverse('book-detail', args=[self.book1.id])

    def test_list_books(self):
        """GET → list all books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book(self):
        """POST → create a new book"""
        data = {
            "title": "Book Three",
            "author": "Author C",
            "publication_year": 2020
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_retrieve_book(self):
        """GET → retrieve a single book"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_update_book(self):
        """PUT → update an existing book"""
        data = {
            "title": "Updated Book One",
            "author": "Author A",
            "publication_year": 2001
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book One")

    def test_delete_book(self):
        """DELETE → remove a book"""
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_title(self):
        """Filter by title query param"""
        response = self.client.get(f"{self.list_url}?title=Book One")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        """Search in title/author"""
        response = self.client.get(f"{self.list_url}?search=Author A")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_year(self):
        """Order results by publication_year"""
        response = self.client.get(f"{self.list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2000)
