from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView (TemplateView):
    template_name = 'home.html'


def ContactView(request):
    return render(request, template_name='pages/contact.html')


def aboutView(request):
    return render(request, template_name='pages/aboutus.html')
