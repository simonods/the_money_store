from django.urls import path

from .views import *

urlpatterns = [
    path('', main_page, name='main_page'),
    path('news/', news, name='news'),
    path('currency/', currency, name='currency'),
    path('about_us/', about_us, name='about_us'),
    path('contact/', contact, name='contact'),

]