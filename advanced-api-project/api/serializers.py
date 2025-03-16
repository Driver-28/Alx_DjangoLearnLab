from rest_framework import serializers
from .models import Author, Book

# Custom Book Serializer using ModelSerializer: Handles book data automatically
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year']

    # Custom validation for 'publication_year' to ensure it's a valid year
    def validate_publication_year(self, value):
        if value.year < 1500:
            raise serializers.ValidationError("Publication year must be after 1500.")
        return value

# Custom Author Serializer using ModelSerializer: Handles author data with nested books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested BookSerializer

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

    # Custom validation for 'name' field (e.g., it must be at least 3 characters long)
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Name must be at least 3 characters long.")
        return value
