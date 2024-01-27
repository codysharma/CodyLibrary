from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.list_catalog, name='list_catalog'),
    path('catalog/create', views.book_create, name='book_create'),
    path('catalog/<int:pk>', views.book_detail, name='book_detail'),
    path('catalog/<int:pk>/edit', views.book_edit, name='book_edit'),
    path('catalog/<int:pk>/delete', views.book_delete, name='book_delete'),
    path('catalog/<int:pk>/borrow', views.book_borrow, name='book_borrow'),
    path('catalog/fiction', views.catalog_fiction, name='catalog_fiction'),
    path('catalog/ushistory', views.catalog_ush, name='catalog_ush'),
    path('catalog/worldhistory', views.catalog_wh, name='catalog_wh'),
    path('catalog/politicalscience', views.catalog_ps, name='catalog_ps'),
    path('catalog/education', views.catalog_edu, name='catalog_edu'),
    path('catalog/architectureandurbanplanning', views.catalog_aup, name='catalog_aup'),
    path('catalog/nonfiction', views.catalog_nf, name='catalog_nf'),
    path('catalog/suggest', views.suggestion_create, name='suggestion_create'),
    path('catalog/search/', views.book_search, name='book_search'),
    path('catalog/create/search/', views.isbn_search, name='isbn_search'),
    path('borrowed/', views.all_borrowed, name='all_borrowed'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my_borrowed'),
    path('authors/create', views.author_create, name='author_create'),
    path('map', views.map, name='map'),
    path('events', views.events_list, name='event_list'),
    path('events/create', views.event_create, name='event_create'),
    path('events/<int:pk>', views.event_detail, name='event_detail'),
    path('events/<int:pk>/edit', views.event_edit, name='event_edit'),
    path('events/<int:pk>/delete', views.event_delete, name='event_delete'),
    path('events/<int:pk>/register', views.event_register, name='event_register'),
    path('myevents/', views.my_events_list.as_view(), name='my_events_list'),
    path('clientcontact/', views.list_contact, name='list_contact'),
    path('clientcontact/<int:pk>/', views.contact_detail, name='contact_detail'),

]