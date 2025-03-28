from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import post

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Adding email field

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PostForm(forms.ModelForms):
    class Meta:
        model = post
        fields = ['title', 'content']
