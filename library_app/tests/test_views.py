import pytest
from library_app.models import Book, Author
from library_app.views import book_detail, list_catalog, catalog_fiction, catalog_ush
from django.urls import reverse
from django.test import RequestFactory

from django.conf import settings

def test_settings_loaded():
    assert settings.configured

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
    assert b'book_not_found' not in response.content

@pytest.mark.django_db
def test_book_detail_view_not_found(rf):
    url = reverse('book_detail', kwargs={'pk': 9999})
    request = rf.get(url)
    response = book_detail(request, 9999)

    # print(response.content.decode())

    assert response.status_code == 200
    assert b'book_not_found' in response.content

# test catalog general
@pytest.mark.django_db
def test_list_catalog(rf):
    url = reverse('list_catalog')
    request = rf.get(url)
    response = list_catalog(request)

    assert response.status_code == 200
    assert b'Browse our Catalog' in response.content

# test each catalog section
@pytest.mark.django_db
def test_catalog_fiction(rf):
    url = reverse('catalog_fiction')
    request = rf.get(url)
    response = catalog_fiction(request)

    assert response.status_code == 200
    assert b'Browse our Fiction Collection' in response.content
    assert b'Browse our Non-Fiction Collection' not in response.content

@pytest.mark.django_db
def test_catalog_ush(rf):
    url = reverse('catalog_ush')
    request = rf.get(url)
    response = catalog_ush(request)

    assert response.status_code == 200
    assert b'Browse our US History Collection' in response.content
    assert b'Browse our Non-Fiction Collection' not in response.content

# test catalog with sample book
# -----------------------------------------------------------Mock this one?
@pytest.mark.django_db
def test_list_catalog_with_example(book_fixture, rf):
    book = book_fixture
    url = reverse('list_catalog')
    request = rf.get(url)
    response = list_catalog(request)

    assert response.status_code == 200
    # assert b'Browse our Catalog' in response.content

# mockup book create form



