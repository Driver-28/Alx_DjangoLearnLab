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
