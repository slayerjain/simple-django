# myapp/tests.py

import datetime
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Book

# ---------------------------------------------------------
# 1. Model Tests
# ---------------------------------------------------------

class BookModelTestCase(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            published_date=datetime.date(2020, 1, 1)
        )

    def test_book_str_representation(self):
        """Test the string representation of the Book model"""
        self.assertEqual(str(self.book), 'Test Book')


# ---------------------------------------------------------
# 2. API Tests (Django REST Framework)
# ---------------------------------------------------------

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create some test data
        self.book1 = Book.objects.create(
            title='Book 1',
            author='Author 1',
            published_date=datetime.date(2021, 1, 1)
        )
        self.book2 = Book.objects.create(
            title='Book 2',
            author='Author 2',
            published_date=datetime.date(2022, 2, 2)
        )

        # URL for list-create endpoint
        self.list_url = reverse('book-list-create')
        # URL pattern for detail endpoint requires an ID; we’ll use self.book1.pk as an example
        self.detail_url = reverse('book-rud', kwargs={'pk': self.book1.pk})

    def test_get_book_list(self):
        """Test GET request to /api/books/ returns list of books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # We created 2 books in setUp()

    def test_create_book(self):
        """Test POST request to /api/books/ creates a new book"""
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'published_date': '2023-01-01'
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)  # 2 from setUp + 1 new

    def test_retrieve_book(self):
        """Test GET request to /api/books/<pk>/ retrieves a specific book"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_update_book(self):
        """Test PUT/PATCH request to /api/books/<pk>/ updates an existing book"""
        data = {
            'title': 'Updated Title',
            'author': 'Updated Author',
            'published_date': '2025-05-05'
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Title')
        self.assertEqual(self.book1.author, 'Updated Author')

    def test_delete_book(self):
        """Test DELETE request to /api/books/<pk>/ deletes an existing book"""
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)  # 2 originally, 1 deleted


# ---------------------------------------------------------
# 3. Template View Tests
# ---------------------------------------------------------

from django.test import Client

class BookTemplateViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.book1 = Book.objects.create(
            title='Template Book 1',
            author='Template Author 1',
            published_date=datetime.date(2021, 1, 1)
        )
        self.book2 = Book.objects.create(
            title='Template Book 2',
            author='Template Author 2',
            published_date=datetime.date(2022, 2, 2)
        )
        self.list_url = reverse('book-list')   # /books/
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})

    def test_book_list_view(self):
        """Test the book list template is rendered correctly"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/book_list.html')
        # Check that the context contains the books
        self.assertContains(response, 'Template Book 1')
        self.assertContains(response, 'Template Book 2')

    def test_book_detail_view(self):
        """Test the book detail template is rendered correctly"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/book_detail.html')
        self.assertContains(response, 'Template Book 1')
        self.assertContains(response, 'Template Author 1')