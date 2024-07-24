from django.contrib import admin
from .models import *


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'last_action_date', 'verification_accepted', 'bottomless_pit')
    list_display_links = ('id', 'username')
    search_fields = ('username',)


class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'price_usdt', 'is_published')
    list_display_links = ('id', 'title', 'category', 'price_usdt')
    search_fields = ('title',)


class CategoryPositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(CategoryPosition, CategoryPositionAdmin)
