from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/create', views.book_create, name='book_create'),
    path('catalog/<int:pk>', views.book_detail, name='book_detail'),
    path('catalog/<int:pk>/edit', views.book_edit, name='book_edit'),
    path('catalog/<int:pk>/delete', views.book_delete, name='book_delete'),
    path('catalog/fiction', views.catalog_fiction, name='catalog_fiction'),
    path('catalog/ushistory', views.catalog_ush, name='catalog_ush'),
    path('catalog/worldhistory', views.catalog_wh, name='catalog_wh'),
    path('catalog/politicalscience', views.catalog_ps, name='catalog_ps'),
    path('catalog/education', views.catalog_edu, name='catalog_edu'),
    path('catalog/architectureandurbanplanning', views.catalog_aup, name='catalog_aup'),
    path('catalog/nonfiction', views.catalog_nf, name='catalog_nf'),
    path('catalog/suggest', views.suggestion_create, name='suggestion_create'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my_borrowed'),
    path('authors/create', views.author_create, name='author_create')
]