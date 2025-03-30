from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework import status, permissions, generics
from .serializers import UserSerializer, PostSerializer
from .models import Post

CustomUser = get_user_model()

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already taken"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.id})
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"token": user.auth_token.key, "user_id": user.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = User.objects.get(id=user_id)
        if user_to_follow == request.user:
            return Response({"error": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}"}, status=status.HTTP_200_OK)

class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = User.objects.get(id=user_id)
        if user_to_unfollow == request.user:
            return Response({"error": "You cannot unfollow yourself"}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.remove(user_to_unfollow)
        return Response({"message": f"You have unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)
class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author__in=user.following.all()).order_by("-created_at")
class UserListView(generics.ListAPIView):
    """Retrieve all users"""
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
