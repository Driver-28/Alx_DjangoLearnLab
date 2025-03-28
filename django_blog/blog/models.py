from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(default=now)
class User(models.Model):
    author = models.ForeignKey(Post, on_delete=models.CASCADE)
