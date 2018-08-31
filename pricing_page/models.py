from __future__ import unicode_literals
from django.db import models
from tinymce.models import HTMLField


class PricingFrontPage(models.Model):
    main_title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)


class Pricing(models.Model):
    pricing_title = models.CharField(max_length=200)
    prices = HTMLField()
