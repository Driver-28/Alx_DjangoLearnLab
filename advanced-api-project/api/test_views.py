from rest_framework import generics
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer
import django_filters
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

# Filter class to filter books by title, author, or publication year
class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')  # Filters by title, case-insensitive
    author = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains')  # Filters by author name, case-insensitive
    publication_year = django_filters.DateFilter(field_name='publication_year', lookup_expr='exact')  # Filters by exact publication year

    class Meta:
        model = Book

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)  # Correct filter usage
    filterset_class = BookFilter  # Custom filter class
    search_fields = ['title', 'author__name']  # Allow searching on title and author name
    ordering_fields = ['title', 'publication_year', 'author__name']  # Allow ordering by title, publication_year, and author name
    ordering = ['title']  # Default ordering by title

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create a book

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update a book

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete a book

class BookTests(APITestCase):

    def setUp(self):
        # Set up some initial data, such as creating a Book instance.
        self.book = Book.objects.create(title="Test Book", author="Test Author", publication_year="2021-01-01")
        self.url = reverse('book-list')  # Adjust according to your URL patterns

    def test_create_book(self):
        # Test creating a book
        data = {
            "title": "New Book",
            "author": "New Author",
            "publication_year": "2022-01-01"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)  # Ensure that the book count increased
        self.assertEqual(Book.objects.latest('id').title, "New Book")  # Ensure that the new book is created

    def test_get_books(self):
        # Test retrieving all books
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Since we have one book in the setup

    def test_update_book(self):
        # Test updating a book
        data = {
            "title": "Updated Book Title",
            "author": "Updated Author",
            "publication_year": "2023-01-01"
        }
        response = self.client.put(reverse('book-detail', args=[self.book.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book Title")

    def test_delete_book(self):
        # Test deleting a book
        response = self.client.delete(reverse('book-detail', args=[self.book.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)  # Ensure the book was deleted
