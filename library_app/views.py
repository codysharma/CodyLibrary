from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import Book, User, Author
# from .serializers import BookSerializer
# from rest_framework import generics
from django.views import View
from django.views.generic.list import ListView
from .forms import BookForm, AuthorForm, SuggestedBookForm, BorrowBookForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models import CharField
from django.db.models.functions import Lower
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from django.core.paginator import Paginator
import requests

CharField.register_lookup(Lower)

# Create your views here.
def index(req):
    staff_list = Book.objects.filter(title="1491: New Revelations of the Americas Before Columbus")
    context = {
        'staff_list': staff_list
    }
    return render(req, 'library_app/index.html', context)

def book_detail(req, pk):
    book = Book.objects.get(id=pk)
    return render(req, 'library_app/catalog/book_detail.html', {'book': book})

def list_catalog(req):
    q = req.GET.get('q')
    query = None

    if q:
        vector = SearchVector('title', 'author__name') 
        # vector = SearchVector('title')
        query = SearchQuery(q)
        results = Book.objects.annotate(search=SearchVector('title','author__name')).filter(Q(search=query) | Q(author__name__icontains=q))
    else:
        results = None

    catalog = Book.objects.all().order_by('title')
    # Pagination
    p = Paginator(catalog, 15)
    page = req.GET.get('page')
    catalog_list = p.get_page(page)
    context = {
        'catalog': catalog,
        'catalog_list': catalog_list,
        'results': results,
        'query': query,
        }
    return render(req, 'library_app/catalog/catalog_base.html', context)

def catalog_fiction(req):
    fiction_catalog = Book.objects.filter(genre="FICT").order_by('title')
    return render(req, 'library_app/catalog/catalog_fiction.html', {'fiction_catalog': fiction_catalog})

def catalog_ush(req):
    ush_catalog = Book.objects.filter(genre="USH").order_by('title')
    return render(req, 'library_app/catalog/catalog_ush.html', {'ush_catalog': ush_catalog})

def catalog_wh(req):
    wh_catalog = Book.objects.filter(genre="WH").order_by('title')
    return render(req, 'library_app/catalog/catalog_wh.html', {'wh_catalog': wh_catalog})

def catalog_ps(req):
    ps_catalog = Book.objects.filter(genre="PS").order_by('title')
    return render(req, 'library_app/catalog/catalog_ps.html', {'ps_catalog': ps_catalog})

def catalog_edu(req):
    edu_catalog = Book.objects.filter(genre="EDU").order_by('title')
    return render(req, 'library_app/catalog/catalog_edu.html', {'edu_catalog': edu_catalog})

def catalog_aup(req):
    aup_catalog = Book.objects.filter(genre="AUP").order_by('title')
    return render(req, 'library_app/catalog/catalog_aup.html', {'aup_catalog': aup_catalog})

def catalog_nf(req):
    nf_catalog = Book.objects.filter(genre="NF").order_by('title')
    return render(req, 'library_app/catalog/catalog_nf.html', {'nf_catalog': nf_catalog})

@login_required
@user_passes_test(lambda u:u.is_staff)
def book_create(req):
    if req.method == 'POST':
        form = BookForm(req.POST)
        if form.is_valid():
            book = form.save()
            return redirect('book_detail', pk=book.pk) 
    else:
        form = BookForm()
        q = req.GET.get('q')

        if q:
            api_url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{q}"
            response = requests.get(api_url)
            json = response.json()
            result = {
                "title": json["items"][0]["volumeInfo"]["title"],
                "author": json["items"][0]["volumeInfo"]["authors"][0],
                "published_date": json["items"][0]["volumeInfo"]["publishedDate"],
                "desription": json["items"][0]["volumeInfo"]["description"],
                "thumbnail": json["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"],
            }
        else:
            result = None
        context = {
            'form': form,
            'result': result
        }
        return render(req, 'library_app/catalog/new_book_form.html', context)

@login_required
@user_passes_test(lambda u:u.is_staff)
def book_edit(req, pk):
    book = Book.objects.get(id=pk)
    if req.method == "POST":
        form = BookForm(req.POST, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(req, 'library_app/catalog/book_edit_form.html', {'form': form, 'book': book})

@login_required
@user_passes_test(lambda u:u.is_staff)
def book_delete(_, pk):
    Book.objects.get(id=pk).delete()
    return redirect('catalog')

@login_required
def book_borrow(req, pk):
    book = Book.objects.get(id=pk)
    if req.method == "POST":
        form = BorrowBookForm(req.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.borrower = req.user
            book.save()
            return redirect('book_detail', pk=book.pk)    
    else:
        form = BorrowBookForm(instance=book)
    context = {
        'form': form, 
        'book': book
    }
    return render(req, 'library_app/catalog/book_borrow_form.html', context)

@login_required
@user_passes_test(lambda u:u.is_staff)
def author_create(req):
    if req.method == 'POST':
            form = AuthorForm(req.POST)
            if form.is_valid():
                book = form.save()
                return redirect('book_create') 
    else:
        form = AuthorForm()
        return render(req, 'library_app/catalog/new_author_form.html', {'form': form})
    
@login_required
def suggestion_create(req):
    if req.method == 'POST':
        form = SuggestedBookForm(req.POST)
        if form.is_valid():
            book = form.save()
            return redirect('catalog') 
    else:
        form = SuggestedBookForm()
        return render(req, 'library_app/suggestion_form.html', {'form': form})
    
def signup(req):
  error_message = ''
  if req.method == 'POST':
    form = UserCreationForm(req.POST)
    if form.is_valid():
      user = form.save()
      login(req, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(req, 'registration/signup.html', context)

class LoanedBooksByUserListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'library_app/book_list_borrowed_user.html'
    
    def get_queryset(self):
        return (
            Book.objects.filter(borrower=self.request.user)
            # From example, if I want to add a due-by date
            # .filter(status__exact='o')
            # .order_by('due_back')
        )

def map(req):
    return render(req, 'library_app/map.html')

def events_list(req):
    return render(req, 'library_app/events_list.html')

@login_required
@user_passes_test(lambda u:u.is_staff)
def all_borrowed(req):
    borrowed_list = Book.objects.filter(borrower__isnull=False)
    return render(req, 'library_app/borrowed_list.html', {'borrowed_list': borrowed_list})

def book_search(req):
    q = req.GET.get('q')
    if q:
        vector = SearchVector('title', 'author__name') 
        # vector = SearchVector('title')
        query = SearchQuery(q)
        results = Book.objects.annotate(search=SearchVector('title','author__name')).filter(Q(search=query) | Q(author__name__icontains=q))
    else:
        results = None
    # return render(req, 'library_app/catalog/search_page.html', {'results': results})
    return results

def isbn_form(req):
    return render (req, 'library_app/catalog/isbn_form.html')

def isbn_search(req, isbn):
    q = req.GET.get('q')
    print(q)
    api_url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    # Test isbn: 9781603842037
    response = requests.get(api_url)
    json = response.json()

    # print(json["items"][0]["volumeInfo"]["title"], json["items"][0]["volumeInfo"]["authors"][0])

    if json:
        result = {
        "title": json["items"][0]["volumeInfo"]["title"],
        "author": json["items"][0]["volumeInfo"]["authors"][0],
        "published_date": json["items"][0]["volumeInfo"]["publishedDate"],
        "desription": json["items"][0]["volumeInfo"]["description"],
        "thumbnail": json["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"],
        }
    else:
        result = None

    return result