from django.contrib import admin
from .models import Books


class Book_admin (admin.ModelAdmin):
    list_display = ('title', 'author',)


admin.site.register(Books, Book_admin)
