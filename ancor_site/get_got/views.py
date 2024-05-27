from django.contrib.auth.views import LoginView, PasswordResetView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import *
from .models import *
from .utils import *


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


def after_login(request):
    return render(request, 'get_got/after_login.html', {'title': 'Solana Market', 'menu': menu, 'username': UserInfo.username})


class LoginUser(DataMixin, LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'get_got/login_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Login')
        return dict(list(context.items()) + list(c_def.items()))

    # def get_success_url(self):
    #     return reverse_lazy('after_login')


class ForgotPassword(DataMixin, PasswordResetView):
    form_class = ForgotPassword
    template_name = 'get_got/forgot_password.html'
    success_url = reverse_lazy('after_login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Forgot password')
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegistrationForm
    template_name = 'get_got/register_page.html'
    success_url = reverse_lazy('after_login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Registration')
        return dict(list(context.items()) + list(c_def.items()))
