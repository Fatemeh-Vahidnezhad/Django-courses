from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Books


class BookListView(generic.ListView):
    model = Books
    paginate_by = 2
    template_name = 'books/books_list.html'
    context_object_name = 'book_lists'


class BookDetailView(generic.DetailView):
    model = Books
    template_name = 'books/books_detail.html'
    context_object_name = 'book'


class CreateBookView(generic.CreateView):
    model = Books
    template_name = 'books/create_books.html'
    fields = ['title', 'author', 'description', 'cover', ]


class UpdateBookView(generic.UpdateView):
    model = Books
    template_name = 'books/update_book.html'
    fields = ['title', 'author', 'description', 'cover', ]


class DeleteBookView(generic.DeleteView):
    model = Books
    template_name = 'books/delete_book.html'
    context_object_name = 'book'
    success_url = reverse_lazy('book_list')
