from django.contrib import admin
from .models import HelloUser

# Register your models here.
# python manage.py createsuperuser : 어드민 계정생성
class HelloUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'userpw')    # admin page 에 보여줄 항목들 설정 가능!

admin.site.register(HelloUser, HelloUserAdmin)    # admin 연결