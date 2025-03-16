from rest_framework import generics
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer
import django_filters

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
