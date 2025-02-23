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
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home page after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Custom Login View using Django's built-in form
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Custom Logout View using Django's built-in logout
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'
