from rest_framework import serializers
from .models import Author, Book, Event

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(
        view_name='book_detail',
        many=True,
        read_only=True,
    )

    author_url = serializers.ModelSerializer.serializer_url_field(
        view_name='author_detail'
    )

    class Meta:
        model = Author
        fields = ('id', 'name', 'nationality', 'books', 'author_url')

class BookSerializer(serializers.HyperlinkedModelSerializer):
    author_name = serializers.CharField(
        source='author.name',
        read_only=True
    )
    
    book_url = serializers.ModelSerializer.serializer_url_field(
        view_name='book_detail'
    )

    class Meta:
        model = Book
        fields = ('id', 'title', 'book_url', 'author_name', 'publication_year', 'genre', 'number_in_collection' )