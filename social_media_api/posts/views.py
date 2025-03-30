from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, generics, status
from .models import Post, Comment, like
from .serializers import PostSerializer, CommentSerializer
from django.contrib.auth import get_user_model
from notifications.models import Notification
from django.shortcuts import get_object_or_404
from rest_framework.generics import get_object_or_404

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Set the author automatically

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Set the author automatically

CustomUser = get_user_model()

class UserFeedView(generics.ListAPIView):
    """Retrieve posts from users the current user follows"""
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Get posts from users that the current user follows"""
        user = self.request.user
        following_users = user.following.all()
         return Post.objects.filter(author__in=following_users).order_by("-created_at")
class LikePostView(generics.GenericAPIView):
    """Handles liking a post"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({"detail": "Already liked this post"}, status=status.HTTP_400_BAD_REQUEST)

        # Create a notification
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            target=post
        )

        return Response({"detail": "Post liked successfully"}, status=status.HTTP_201_CREATED)


class UnlikePostView(generics.GenericAPIView):
    """Handles unliking a post"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post)

        if like.exists():
            like.delete()
            return Response({"detail": "Post unliked successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "You haven't liked this post"}, status=status.HTTP_400_BAD_REQUEST)     
class PostDetailView(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
