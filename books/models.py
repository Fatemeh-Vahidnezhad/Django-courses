from django.db import models
from django.urls import reverse


class Books(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='covers/', blank=True)
    translator = models.CharField(max_length=200, blank=True)
    publisher = models.CharField(max_length=200, blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])









