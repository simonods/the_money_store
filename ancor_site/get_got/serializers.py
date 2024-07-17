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


class PositionSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    describe = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=False)
    category = serializers.PrimaryKeyRelatedField(queryset=CategoryPosition.objects.all())
    price_usdt = serializers.DecimalField(max_digits=27, decimal_places=8)

    def create(self, validated_data):
        return Position.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.describe = validated_data.get('describe', instance.describe)
        instance.time_create = validated_data.get('time_create', instance.time_create)
        instance.time_update = validated_data.get('time_update', instance.time_update)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.category = validated_data.get('category', instance.category)
        instance.price_usdt = validated_data.get('price_usdt', instance.price_usdt)
        instance.save()
        return instance

    class Meta:
        fields = ('title', 'category', 'price_usdt')
