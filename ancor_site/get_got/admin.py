from django.contrib import admin

from .models import *


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'last_action_date', 'verification_accepted', 'bottomless_pit')
    list_display_links = ('id', 'username')
    search_fields = ('username',)


admin.site.register(UserInfo, UserInfoAdmin)
