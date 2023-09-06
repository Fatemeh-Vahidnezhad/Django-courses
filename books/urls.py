from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('create/', views.CreateBookView.as_view(), name='create_book'),
    path('<int:pk>/edit/', views.UpdateBookView.as_view(), name='update_book'),
    path('<int:pk>/delete/', views.DeleteBookView.as_view(), name='delete_book'),

]
