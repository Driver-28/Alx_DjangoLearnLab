from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["id", "username", "email", "bio", "profile_picture", "followers", "password"]
    def create(self, validated_data):
        """Create a new user and generate a token."""
        password = serializers.CharField(write_only=True)
        user = get_user_model().objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data.get("email", ""),
        )
        Token.objects.create(user=user)  # Generate authentication token
        return user
