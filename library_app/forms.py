from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title','publication_year','author','genre', 'number_in_collection', 'picture_url')