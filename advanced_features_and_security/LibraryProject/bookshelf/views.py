from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # Process the form and update the book
        book.title = request.POST['title']
        book.save()
    return render(request, 'edit_book.html', {'book': book})

@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'view_book.html', {'book': book}

)
from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'book_list.html', {'books': books})

from django.shortcuts import render
from .forms import ExampleForm

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process form data here (e.g., save it to the database, send an email, etc.)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Do something with the data, e.g., save to the database
            return render(request, 'bookshelf/form_success.html', {'name': name})
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})
