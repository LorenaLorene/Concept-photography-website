from django.contrib import admin
from .models import ContactInfo


class ContactInfoAdmin(admin.ModelAdmin):
    model = ContactInfo
    list_display = ['phone', 'email', 'address']


admin.site.register(ContactInfo, ContactInfoAdmin)

