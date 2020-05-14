from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stuck', 'reg_date')

admin.site.register(Product, ProductAdmin)