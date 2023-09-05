from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('contact/', views.ContactView, name='contactus'),
    path('about/', views.aboutView, name='aboutus'),
]