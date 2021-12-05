from django.shortcuts import render

from .models import GalleryItem


def gallery_page(request):
    items = GalleryItem.objects.all()
    return render(request, 'gallery.html', {'items': items})
