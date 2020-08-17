from django.contrib import admin
from .models import FcUser

# Register your models here.
class FcUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'level')

admin.site.register(FcUser, FcUserAdmin)