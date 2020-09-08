from django.contrib import admin
from .models import Content, Image, FollowReleation

# Register your models here.
class ImageInline(admin.TabularInline):
    model = Image


class ContentAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('user', 'created_at')

admin.site.register(Content, ContentAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'created_at')

admin.site.register(Image, ImageAdmin)


class FollowRelationAdmin(admin.ModelAdmin):
    list_display = ('follower', 'created_at')

admin.site.register(FollowReleation, FollowRelationAdmin)