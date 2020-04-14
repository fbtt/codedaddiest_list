import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
# Create your views here.

def home(request):
    return render(request, template_name='base.html')


def new_search(request):
    search = request.POST.get('search')
    stuff_from_frontend = {
        'search': search,
    }
    print(stuff_from_frontend['search'])
    return render(request, template_name='my_app/new_search.html', context=stuff_from_frontend)