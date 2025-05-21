from rest_framework import serializers
from .models import Author, Book, Event

class BookSerializer(serializers.HyperlinkedModelSerializer):
    author_name = serializers.CharField(
        source='author.name',
        read_only=True
    )
    
    # book_url = serializers.ModelSerializer.serializer_url_field(
    #     view_name='book_detail'
    # )

    class Meta:
        model = Book
        fields = ('id', 'title', 'author_name', 'publication_year', 'genre', 'number_in_collection' )

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'date', 'description')