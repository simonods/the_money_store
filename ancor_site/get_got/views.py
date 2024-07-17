from django.contrib.auth.views import LoginView, PasswordResetView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from rest_framework import viewsets, generics
from django.contrib.auth import get_user_model, logout
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
    return render(request, 'get_got/after_login.html', {'title': 'Solana Market', 'menu': menu, 'username': UserInfo.username})


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


class PositionAPIView(APIView):
    def get(self, request):
        pos = Position.objects.all()
        return Response({'positions': PositionSerializer(pos, many=True).data})

    def post(self, request):
        serialzer = PositionSerializer(data=request.data)
        serialzer.is_valid(raise_exception=True)
        serialzer.delete()

        return Response({'post': serialzer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})

        try:
            instance = Position.objects.get(pk=pk)
        except:
            return Response({'error': 'object does not exist'})

        serializer = PositionSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method Delete not allowed'})

        try:
            instance = Position.objects.get(pk=pk)
            instance.delete()
            return Response({'post': 'delete post in try ' + str(pk)})

        except:
            return Response({'error': 'object does not exist'})
