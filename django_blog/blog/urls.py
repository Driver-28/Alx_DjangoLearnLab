from django.contrib.auth import views as auth_views
from . import views
from django.urls import path

urlpatterns = [
    # Other URLs
    path('login/', auth_views.LoginView.as_view(), name='login'),
]

urlpatterns = [
    # Other URLs
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

urlpatterns = [
    # Login, Logout, and Registration views
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),  # For profile view
]

urlpatterns = [
    # Other URL patterns
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]
