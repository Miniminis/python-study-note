from django.contrib import admin
from .models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'reg_date')

admin.site.register(Order, OrderAdmin)