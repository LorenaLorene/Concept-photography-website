from __future__ import unicode_literals

from django.db import models


from phonenumber_field.modelfields import PhoneNumberField




class ContactInfo(models.Model):
    phone = PhoneNumberField()


