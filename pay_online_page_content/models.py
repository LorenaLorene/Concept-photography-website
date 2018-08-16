from __future__ import unicode_literals
from django.db import models
from tinymce.models import HTMLField


class PayOnlineFrontPage(models.Model):
    main_title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = HTMLField()


class PayOnlineNote(models.Model):
    please_note = HTMLField()

