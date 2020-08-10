from django.contrib import admin
from .models import FcMallProduct

# Register your models here.
class FcProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(FcMallProduct, FcProductAdmin)
