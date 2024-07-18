from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'birth_date']


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'content', 'pub_date')


class PositionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Position
        # fields = ('title', 'category', 'price_usdt')
        fields = '__all__'
