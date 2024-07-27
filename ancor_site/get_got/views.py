import json
import os
import requests

from django.contrib.auth.views import LoginView, PasswordResetView
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView, TemplateView
from django.contrib.auth import get_user_model, logout

from rest_framework import viewsets, generics
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .forms import *
from .models import *
from .utils import *
from .coin_market_cup import api_key, api_url

User = get_user_model()


def main_page(request):
    return render(request, 'get_got/main_page.html', context=(get_data_context()))


def news(request):
    return render(request, 'get_got/news.html', context=(get_data_context()))


def currency(request):
    return render(request, 'get_got/currency.html', context=(get_data_context()))


def about_us(request):
    return render(request, 'get_got/about_us.html', context=(get_data_context()))


def contact(request):
    return render(request, 'get_got/contact.html', context=(get_data_context()))


def nft_uranus(request):
    return render(request, 'get_got/nft_generator.html', context=(get_data_context()))


def after_login(request):
    return render(request, 'get_got/after_login.html',
                  context=DataMixin.get_user_context(request))


# User AUTH
class LoginUser(DataMixin, LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'get_got/login_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Login')
        return dict(list(context.items()) + list(c_def.items()))


def logout_user(request):
    logout(request)
    return redirect('main_page')


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


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ArticleAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CoinMarketCupAPIDataView(generics.ListAPIView):
    def get(self, request):
        url = api_url
        # url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': api_key,
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        return Response(data)


def coin_market_cap(request):
    return render(request, 'get_got/cmc_test.html', context=get_data_context())


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class MarketplacePositionsView(DataMixin, TemplateView):
    template_name = 'get_got/the_money_store.html'
    serializer = PositionSerializer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        positions = Position.objects.all()

        # Додаємо пагінацію
        page = self.request.GET.get('page', 1)
        per_page = self.request.GET.get('per_page', 5)
        try:
            per_page = int(per_page)
        except ValueError:
            per_page = 5
        paginator = Paginator(positions, per_page)
        page_obj = paginator.get_page(page)

        context['positions'] = positions
        context['per_page'] = per_page
        context['page_obj'] = page_obj

        return context


class PositionAPIList(generics.ListCreateAPIView):  # GET, POST requests
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class PositionAPIUpdate(generics.UpdateAPIView):  # PUT, PATCH requests
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class PositionAPIDetail(generics.RetrieveUpdateDestroyAPIView):  # GET, PUT, PATCH, DELETE requests
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
