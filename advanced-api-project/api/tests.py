from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Book
from rest_framework.permissions import IsAuthenticated

class BookTests(APITestCase):

    # Test Book Creation
    def test_create_book(self):
        url = reverse('book-create')  # The URL for the BookCreateView
        data = {'title': 'Test Book', 'author': 'Test Author', 'publication_year': '2025-01-01'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'Test Book')

    # Test Book Update
    def test_update_book(self):
        book = Book.objects.create(title='Old Title', author='Author', publication_year='2020-01-01')
        url = reverse('book-update', args=[book.id])  # The URL for the BookUpdateView
        data = {'title': 'Updated Title', 'author': 'Updated Author', 'publication_year': '2023-01-01'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book.refresh_from_db()
        self.assertEqual(book.title, 'Updated Title')

    # Test Book Deletion
    def test_delete_book(self):
        book = Book.objects.create(title='Book to Delete', author='Author', publication_year='2020-01-01')
        url = reverse('book-delete', args=[book.id])  # The URL for the BookDeleteView
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # Test Filtering Books
    def test_filter_books(self):
        Book.objects.create(title='Book One', author='Author One', publication_year='2020-01-01')
        Book.objects.create(title='Book Two', author='Author Two', publication_year='2021-01-01')

        url = reverse('book-list') + '?title=Book One'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # Test Search Books
    def test_search_books(self):
        Book.objects.create(title='Searchable Book', author='Searchable Author', publication_year='2020-01-01')
        url = reverse('book-list') + '?search=Searchable'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # Test Order Books
    def test_order_books(self):
        Book.objects.create(title='A Book', author='Author A', publication_year='2020-01-01')
        Book.objects.create(title='B Book', author='Author B', publication_year='2021-01-01')

        url = reverse('book-list') + '?ordering=title'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'A Book')

    # Test Unauthorized Access
    def test_create_book_without_authentication(self):
        url = reverse('book-create')
        data = {'title': 'Test Book', 'author': 'Test Author', 'publication_year': '2025-01-01'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
