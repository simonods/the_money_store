from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name='main_page'),
    path('news/', news, name='news'),
    path('currency/', currency, name='currency'),
    path('about_us/', about_us, name='about_us'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('forgot_password/', ForgotPassword.as_view(), name='forgot_password'),
    path('after_login/', after_login, name='after_login'),
]
