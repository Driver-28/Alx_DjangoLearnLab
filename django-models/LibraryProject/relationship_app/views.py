from django.shortcuts import render
from django.shortcuts import render, get_object_or_40i4
from django.views.generic.detail import DetailView
from .models import Library  # Explicitly import Library
from .models import Book, Library

# Function-based view: List all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based view: Library detail
class LibraryDetailView(DetailView):
    model = Library  # Library model explicitly used
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_object(self):
        library_id = self.kwargs.get("pk")
        return get_object_or_404(Library, pk=library_id)

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Register view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Home view (for testing redirection after login)
def home(request):
    return render(request, 'relationship_app/home.html', {'user': request.user})
