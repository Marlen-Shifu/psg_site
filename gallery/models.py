from django.db import models


class GalleryItem(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'


class GalleryPhoto(models.Model):
    galleryitem = models.ForeignKey(GalleryItem, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='gallery')

