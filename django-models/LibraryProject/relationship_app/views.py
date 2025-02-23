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
from django.contrib.auth.views import LoginView, LogoutView

# Registration View
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

# LoginView and LogoutView are already set in urls.py using custom templates

# Home view (for testing)
def home(request):
    return render(request, 'relationship_app/home.html', {'user': request.user})

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required

# Helper function to check user roles
def check_role(role):
    def role_checker(user):
        return user.is_authenticated and user.userprofile.role == role
    return role_checker

# Admin View
@user_passes_test(check_role('Admin'))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {'role': 'Admin'})

# Librarian View
@user_passes_test(check_role('Librarian'))
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html', {'role': 'Librarian'})

# Member View
@user_passes_test(check_role('Member'))
def member_view(request):
    return render(request, 'relationship_app/member_view.html', {'role': 'Member'})
