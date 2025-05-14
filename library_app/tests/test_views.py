import pytest
from library_app.models import Book, Author
from library_app.views import book_detail
from django.urls import reverse
from django.test import RequestFactory

@pytest.fixture
def book_fixture(db):
    author = Author.objects.create(name="Test Author")

    return Book.objects.create(
        title = "Test Book", 
        author = author, 
        publication_year = 2023,
        number_in_collection = 1,
        genre="Fiction",)

@pytest.mark.django_db
def test_book_detail_view(book_fixture, rf):
    book = book_fixture
    url = reverse('book_detail', kwargs={'pk': book.id})
    
    request = rf.get(url)
    response = book_detail(request, book.id)
    
    assert response.status_code == 200
    assert b'book' in response.content
    assert book.title.encode() in response.content

@pytest.mark.django_db
def test_book_detail_view_not_found(rf):
    url = reverse('book_detail', kwargs={'pk': 9999})
    request = rf.get(url)
    response = book_detail(request, 9999)

    # assert not b'book' in response.content

