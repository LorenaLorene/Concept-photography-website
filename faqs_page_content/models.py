from __future__ import unicode_literals


from django.db import models


from tinymce.models import HTMLField


class PhotographyFaqs(models.Model):
    title = models.CharField(max_length=200)
    faqs = HTMLField()


