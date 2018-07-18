from __future__ import unicode_literals
from django.db import models


class HomeFrontPage(models.Model):
    main_title = models.CharField(max_length=200)
    small_title = models.CharField(max_length=200)
    image = models.FileField(upload_to='assets/images')


class CompanyVision(models.Model):
    title = models.CharField(max_length=200)
    vision = models.CharField(max_length=200)
    image = models.FileField(upload_to='assets/images')


class ShootCount(models.Model):
    count_title = models.CharField(max_length=200)
    description_field = models.CharField(max_length=200)
    image = models.FileField(upload_to='assets/images')


class PhotographersCount(models.Model):
    count_title = models.CharField(max_length=200)
    description_field = models.CharField(max_length=200)


class OurService(models.Model):
    main_title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description_field = models.CharField(max_length=200)
    image = models.FileField(upload_to='assets/images')


