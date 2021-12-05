from django.contrib import admin
from .models import GalleryItem, GalleryPhoto


class GalleryPhotoInline(admin.TabularInline):
    model = GalleryPhoto


class GalleryItemAdmin(admin.ModelAdmin):
    inlines = [
        GalleryPhotoInline
    ]


admin.site.register(GalleryItem, GalleryItemAdmin)