from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
import django_filters
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
from rest_framework.filters import OrderingFilter, SearchFilter

# Create your views here.
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Create a filter class to define the fields that can be filtered
class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')  # Filters by title, case-insensitive
    author = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains')  # Filters by author name, case-insensitive
    publication_year = django_filters.DateFilter(field_name='publication_year', lookup_expr='exact')  # Filters by exact publication year

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

# Create a custom BookListView that includes filtering functionality
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend,)  # Enable filtering
    filterset_class = BookFilter  # Use the BookFilter to define the filters
    search_fields = ['title', 'author__name']
    # Define the ordering fields (e.g., title, publication_year)
    ordering_fields = ['title', 'publication_year', 'author__name']
    ordering = ['title']  # Default ordering (can be adjusted as per preference)
