from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serialize_class = BookSerializer


from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import YourModel
from .serializers import YourModelSerializer

class YourModelViewSet(ModelViewSet):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer
    permission_classes = [IsAuthenticated]
