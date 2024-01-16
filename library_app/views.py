from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from django.views import View
from django.views.generic.list import ListView
from .forms import BookForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def index(req):
    return render(req, 'library_app/index.html')

# class book_detail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

def book_detail(req, pk):
    book = Book.objects.get(id=pk)
    return render(req, 'library_app/catalog/book_detail.html', {'book': book})

def catalog(req):
    catalog = Book.objects.all().order_by('title')
    return render(req, 'library_app/catalog/catalog_base.html', {'catalog': catalog})

def catalog_fiction(req):
    fiction_catalog = Book.objects.filter(genre="FICT").order_by('author')
    return render(req, 'library_app/catalog/catalog_fiction.html', {'fiction_catalog': fiction_catalog})

def catalog_ush(req):
    ush_catalog = Book.objects.filter(genre="USH").order_by('author')
    return render(req, 'library_app/catalog/catalog_ush.html', {'ush_catalog': ush_catalog})

def catalog_wh(req):
    wh_catalog = Book.objects.filter(genre="WH")
    return render(req, 'library_app/catalog/catalog_wh.html', {'wh_catalog': wh_catalog})

def catalog_ps(req):
    ps_catalog = Book.objects.filter(genre="PS")
    return render(req, 'library_app/catalog/catalog_ps.html', {'ps_catalog': ps_catalog})

def catalog_edu(req):
    edu_catalog = Book.objects.filter(genre="EDU")
    return render(req, 'library_app/catalog/catalog_edu.html', {'edu_catalog': edu_catalog})

def catalog_aup(req):
    aup_catalog = Book.objects.filter(genre="AUP")
    return render(req, 'library_app/catalog/catalog_aup.html', {'aup_catalog': aup_catalog})

def catalog_nf(req):
    nf_catalog = Book.objects.filter(genre="NF")
    return render(req, 'library_app/catalog/catalog_nf.html', {'nf_catalog': nf_catalog})

@login_required
def book_create(req):
    if req.method == 'POST':
        form = BookForm(req.POST)
        if form.is_valid():
            book = form.save()
            return redirect('book_detail', pk=book.pk) 
    else:
        form = BookForm()
        return render(req, 'library_app/catalog/new_book_form.html', {'form': form})

@login_required
def book_edit(req, pk):
    print(f"the pk is: {pk}")
    book = Book.objects.get(id=pk)
    print(f"the book id is: {book.id}")
    if req.method == "POST":
        form = BookForm(req.POST, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(req, 'library_app/catalog/book_edit_form.html', {'form': form})

@login_required
def book_delete(_, pk):
    Book.objects.get(id=pk).delete()
    return redirect('catalog')

@login_required
def suggestion_create(req):
    return
    
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
