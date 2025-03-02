# LibraryProject/bookshelf/forms.py

from django import forms

class BookSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Search for Books")
# LibraryProject/bookshelf/forms.py

from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(widget=forms.Textarea, label='Your Message')
