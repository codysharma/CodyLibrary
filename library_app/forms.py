from django import forms
from .models import Book, Author, User

class BookForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.order_by("name"))

    class Meta:
        model = Book
        fields = ('title','publication_year','author','genre', 'location', 'number_in_collection', 'picture_url')

class SuggestedBookForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.order_by("name"))
    
    class Meta:
        model = Book
        fields = ('title', 'publication_year', 'author', 'picture_url')

class BorrowBookForm(forms.ModelForm):
    borrower = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        borrower = kwargs.pop('borrower')
        super(BorrowBookForm, self).__init__(*args, **kwargs)

        if borrower:
            self.fields['borrower'].choices = [(borrower, borrower)]
    
    class Meta:
        model = Book
        fields = ('borrower',)

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'nationality')