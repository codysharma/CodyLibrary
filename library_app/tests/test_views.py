import pytest
from library_app.models import Book
from library_app.views import book_detail
from django.urls import reverse
from django.test import RequestFactory

@pytest.fixture
def book_fixture(db):
    return Book.objects.create(
        title = "Test Book", 
        author=  "Test Author", 
        published_date = "2023-01-01",
        number_in_collection = 1,
        genre="Fiction",)

@pytest.mark.django_db
def test_book_detail_view(book_fixture, rf):
    book = book_fixture
    url = reverse('book-detail', kwargs={'pk': book.id})
    
    request = rf.get(url)
    response = book_detail(request, book.id)
    
    assert response.status_code == 200
    assert 'book' in response.context
    assert response.context['book'] == book

