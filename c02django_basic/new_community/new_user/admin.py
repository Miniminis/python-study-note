from django.contrib import admin
from .models import NewUser

# Register your models here.

class NewuserAdmin(admin.ModelAdmin):
    # user table 에서 list에 표시할 데이터들 
    list_display = ('username', 'password')

admin.site.register(NewUser, NewuserAdmin)