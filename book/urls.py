from django.urls import path 
from .views import book_list, add_book , edit_book


urlpatterns = [
    path('books/', book_list , name = 'book_list'),
    path('books/add/', add_book , name = 'add_book' ),
    path('books/edit/<int:book_id>/' , edit_book , name = 'edit_book'),
]