from django.contrib import admin
from .models import TPost

# Register your models here.
class TPostAdmin(admin.ModelAdmin):
    list_display = ('writer', 'title', 'created_at', 'modified_at')

admin.site.register(TPost, TPostAdmin)