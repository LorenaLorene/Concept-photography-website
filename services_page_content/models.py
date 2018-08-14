from __future__ import unicode_literals
from django.db import models


class ServicesFrontPage(models.Model):
    main_title = models.CharField(max_length=200)
    description_field = models.CharField(max_length=500)


class Service(models.Model):
    title = models.CharField(max_length=200)
    description_field = models.CharField(max_length=600)
    image = models.FileField(upload_to='assets/images')
