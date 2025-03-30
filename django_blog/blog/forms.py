from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import post
from .models import Comment
from taggit.forms import TagWidget

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Adding email field

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PostForm(forms.ModelForms):
    tags = forms.CharField(required=False, widgets=TagWidget(), help_text="Separate tags with commas.")
    class Meta:
        model = post
        fields = ['title', 'content', 'tags']
    def clean_tags(self):
        tags = self.cleaned_data['tags']
        return [tag.strip() for tag in tags.split(',') if tag.strip()]
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
