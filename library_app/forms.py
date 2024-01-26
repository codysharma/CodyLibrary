from django import forms
from .models import Book, Author, User, Event
from django.contrib.auth.models import User

class BookForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.order_by("name"))

    class Meta:
        model = Book
        fields = ('title','publication_year','author','genre', 'location', 'number_in_collection', 'description', 'picture_url', 'borrower', 'staff_blurb')

class SuggestedBookForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.order_by("name"))
    
    class Meta:
        model = Book
        fields = ('title', 'publication_year', 'author', 'picture_url')

class BorrowBookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ()
        # Could implement an until date field as well

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'nationality')

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'date', 'description')
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class EventRegisterForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ()