from django.db import models
from django.urls import reverse


class Books(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=200)
    pages = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])







