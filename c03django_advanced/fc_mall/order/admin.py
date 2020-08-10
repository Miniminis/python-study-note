from django.contrib import admin
from .models import FcMallOrder

# Register your models here.
class FcOrderAdmin(admin.ModelAdmin):
    list_display=('fcuser', 'product')

admin.site.register(FcMallOrder, FcOrderAdmin)