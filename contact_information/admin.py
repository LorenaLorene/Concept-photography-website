from django.contrib import admin

from .models import ContactInfo



class ContactInfoAdmin(admin.ModelAdmin):
    model = ContactInfo
    list_display = ['phone']

admin.site.register(ContactInfo, ContactInfoAdmin)

