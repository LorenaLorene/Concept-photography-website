from __future__ import unicode_literals
from django.db import models


class GalleryFrontPage(models.Model):
    main_title = models.CharField(max_length=200)
    description_field = models.CharField(max_length=200)


class GalleryImage(models.Model):
    image = models.FileField(upload_to='assets/images')
