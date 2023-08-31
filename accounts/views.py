from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import CustomUser
from .form import CustomUserCreationForm


class SignupViews(generic.CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')



