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
    pass

admin.site.register(Image, ImageAdmin)


class FollowReleationAdmin(admin.ModelAdmin):
    pass

admin.site.register(FollowReleation, FollowReleationAdmin)