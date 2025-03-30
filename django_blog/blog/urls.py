from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, CommentUpdateView, CommentDeleteView, PostByTagView

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
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),  # For profile view
]

urlpatterns = [
    # Other URL patterns
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='tagged-posts'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

urlpatterns = [
    # Other URL patterns...
    path('comment/<int:pk>/update/','post/<int:pk>/comments/new/', CommentUpdateView.as_view(), name='comment-edit'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
