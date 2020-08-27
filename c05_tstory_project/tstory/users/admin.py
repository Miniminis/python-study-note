from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


# Register your models here.
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'date_joined')

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
