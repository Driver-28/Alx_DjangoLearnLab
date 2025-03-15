from rest_framework import serializers
from .models import Author, Book
# custom Book Serializer: A manual serializer to handle book data
class BookSerializer(serializers.Serializer):
    #the 'id' field will be read_only and not modifiable
    id = serializers.IntegerField(read_only=True)
    #'title' field store the title of the book
    title = serializers.CharField(max_length=200)
    #'publication_year' field to store the publication year of the book
    publication_year = serializers.DateField()
    #'create' method to create a new Book instance with the validated data 
    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    #'update' method to update an existing Book instance with new validated data
    def update(self, validated_date):
        # Update 'title' and 'publication_year' if they are provided
        instance.title = validated_data.get('title, instance.title')
        instance.publication_year = validated_data.get('publication_year',instance.publication_year)
        # Save the updated instance to the database
        instance.save()
        return instance
# Custom Author Serializer: A manual serializer to handle author data, with nested BookSerializer for related books
class AuthorSerializer(serializers.Serializer):
    # The 'id' field will be read-only and not modifiable
    id = serializers.IntegerField(read_only=True)
    # 'name' field to store the name of the author
    name = serializers.CharField(max_length=200)
    # 'books' field will serialize all related books using the nested BookSerializer
    books = BookSerializer(many=True, read_only=True)

    # 'create' method to create a new Author instance with the validated data
    def create(self, validated_data):
        return Author.objects.create(**validated_data)
    # 'update' method to update an existing Author instance with new validated data
    def update(self, instance, validated_data):
        # Update 'name' if it is provided
        instance.name = validated_data.get('name', instance.name)
        # Save the updated instance to the database
        instance.save()
        return instance
