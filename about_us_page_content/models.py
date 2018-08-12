from __future__ import unicode_literals
from django.db import models
from tinymce.models import HTMLField


class AboutUsFrontPage(models.Model):
    main_title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description_field = models.CharField(max_length=1000)
    office_hours = HTMLField()


class MeetOurTeam(models.Model):
    title = models.CharField(max_length=200)


class OurTeam(models.Model):
    occupation = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    image = models.FileField(upload_to='assets/images')


class CustomerServiceTeam(models.Model):
    main_title = models.CharField(max_length=200)
    description_field = models.CharField(max_length=500)
    image = models.FileField(upload_to='assets/images')


class Testimonial(models.Model):
    testimonials = HTMLField()
