from django.shortcuts import render
from django.views import generic

from .models import Books


class BookListView(generic.ListView):
    model = Books
    template_name = 'books/books_list.html'
    context_object_name = 'book_lists'


class BookDetailView(generic.DetailView):
    model = Books
    template_name = 'books/books_detail.html'
    context_object_name = 'book'


