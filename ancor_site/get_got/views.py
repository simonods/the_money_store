import requests

from django.contrib.auth.views import LoginView, PasswordResetView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView, TemplateView
from django.contrib.auth import get_user_model, logout

from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .forms import *
from .models import *
from .utils import *

User = get_user_model()


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


def nft_uranus(request):
    return render(request, 'get_got/nft_generator.html', {'title': 'Solana Market', 'menu': menu})


def after_login(request):
    return render(request, 'get_got/after_login.html',
                  {'title': 'Solana Market', 'menu': menu, 'username': UserInfo.username})


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


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class MarketplacePositionsView(DataMixin, TemplateView):
    template_name = 'get_got/the_money_store.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        api_url = 'http://127.0.0.1:8000/api/v1/positions/'

        page = self.request.GET.get('page', 1)
        per_page = self.request.GET.get('per_page', 10)

        response = requests.get(api_url)

        # Проверка успешности запроса
        if response.status_code == 200:
            data = response.json()
            # Извлечение списка товаров из ключа 'results'
            products = data.get('results', [])
        else:
            products = []

        # Пагинация
        paginator = Paginator(products, per_page)
        page_obj = paginator.get_page(page)

        # Добавление данных в контекст
        context['page_obj'] = page_obj
        context['per_page'] = per_page
        return context



class ImageUploadView(FormView):  # GPT
    template_name = 'get_got/upload.html'
    form_class = ImageForm
    success_url = reverse_lazy('images')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ImageListView(ListView):  # GPT
    model = Position
    template_name = 'get_got/image_list.html'
    context_object_name = 'images'


class PositionAPIList(generics.ListCreateAPIView):  # GET, POST requests
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class PositionAPIUpdate(generics.UpdateAPIView):  # PUT, PATCH requests
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class PositionAPIDetail(generics.RetrieveUpdateDestroyAPIView):  # GET, PUT, PATCH, DELETE requests
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
