from django.contrib.auth.models import AbstractUser
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.IntegerField()
# Create your models here.
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)  # Date of birth field
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)  # Profile photo field

    def __str__(self):
        return self.username  # Display username in admin interface
# bookshelf/models.py
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)  # Normalize the email address
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)  # Set the password correctly
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """
        Create and return a superuser with an email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)  # Date of birth field
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)  # Profile photo field

    objects = CustomUserManager()  # Set the custom manager

    def __str__(self):
        return self.username

