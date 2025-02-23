from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # Function-based view URL
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view URL
]

from django.urls import path
from .views import register, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]

from django.urls import path
from . import views  # Import your views
from django.contrib.auth.views import LoginView, LogoutView  # Import built-in auth views

urlpatterns = [
    # Registration view
    path('register/', views.register, name='register'),

    # Login and Logout views with custom templates
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
    # Home view (optional for testing redirection after login)
    path('', views.home, name='home'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
]
