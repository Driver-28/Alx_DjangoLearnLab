from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view: List all books
def list_books(request):
    books = Book.objects.all()  # Query all books
    return render(request, 'list_books.html', {'books': books})


# Class-based view: Display details for a specific library
class LibraryDetailView(DetailView):
    model = Library  # Model to use
    template_name = 'library_detail.html'  # Template to render
    context_object_name = 'library'  # Name for use in template

    def get_object(self):
        library_id = self.kwargs.get("pk")  # Get library ID from URL
        return get_object_or_404(Library, pk=library_id)
