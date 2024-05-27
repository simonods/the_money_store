from django.http import HttpResponseNotFound, request
from django.shortcuts import render

# Create your views here.

menu = ['Main Page', 'News', 'Currency', 'About Us', 'Contact']

def main_page(request):
    return render(request, 'get_got/main_page.html', {'title': 'Solana Market', 'menu': menu})

def news(request):
    return render(request, 'get_got/news.html', {'title': 'Solana Market', 'menu': menu})

def currency(request):
    return render(request, 'get_got/currency.html', {'title': 'Solana Market', 'menu': menu})

def about_us(request):
    return render(request, 'get_got/about_us.html', {'title': 'Solana Market', 'menu': menu})

def contact(request):
    return render(request, 'get_got/contact.html', {'title': 'Solana Market', 'menu': menu})


# def pageNotFound(request, exception):
#     return HttpResponseNotFound('<h1> Page not found </h1>')