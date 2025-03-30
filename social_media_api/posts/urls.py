from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from django.urls import path
from .views import UserFeedView, LikePostView, UnlikePostView
from . import views

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
urlpatterns = [
    path("feed/", UserFeedView.as_view(), name="user-feed"),
]
urlpatterns = [
    path("posts/<int:pk>/like/", LikePostView.as_view(), name="post-like"),
    path("posts/<int:pk>/unlike/", UnlikePostView.as_view(), name="post-unlike"),
]
urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
]
