import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_name.settings')  # Replace project_name with your actual project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()  # Using related_name from ForeignKey
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name '{author_name}'.")


# List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # Using ManyToManyField
        print(f"Books in '{library_name}' Library:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'.")


# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # Using OneToOneField related_name
        print(f"Librarian for '{library_name}' Library: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library_name}' Library.")


# Testing the functions with sample data
if __name__ == "__main__":
    # Replace the values with actual data from your database
    get_books_by_author("George Orwell")
    get_books_in_library("Central Library")
    get_librarian_for_library("Central Library")
