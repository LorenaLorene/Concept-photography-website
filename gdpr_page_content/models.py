from __future__ import unicode_literals


from django.db import models


from tinymce.models import HTMLField


class Gdpr(models.Model):
    main_title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    small_title = models.CharField(max_length=200)
    gdpr_content = HTMLField()
