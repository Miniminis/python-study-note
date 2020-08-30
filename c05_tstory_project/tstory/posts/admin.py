from django.contrib import admin
from .models import TPost, TComment

# Register your models here.
class TPostAdmin(admin.ModelAdmin):
    list_display = ('writer', 'title', 'created_at', 'modified_at')

class TCommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'post', 'writer', 'created_at')

admin.site.register(TPost, TPostAdmin)
admin.site.register(TComment, TCommentAdmin)
