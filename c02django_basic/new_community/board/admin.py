from django.contrib import admin
from .models import NewBoard

# Register your models here.
class NewBoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'content', 'reg_date')

admin.site.register(NewBoard, NewBoardAdmin) 