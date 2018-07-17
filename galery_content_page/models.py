from __future__ import unicode_literals

from django.db import models



class GaleryFrontPage(models.Model):
    main_title = models.CharField(max_length=200)
    description_field = models.CharField(max_length=200)


class GaleryImages(models.Model):
    image = models.FileField(upload_to='assets/images')
