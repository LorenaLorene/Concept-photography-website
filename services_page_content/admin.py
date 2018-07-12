from __future__ import unicode_literals

from django.contrib import admin

from .models import ServicesFrontPage
from .models import Services






class ServicesFrontPageAdmin(admin.ModelAdmin):
    model = ServicesFrontPage
    list_display = ['main_title', 'description_field']


admin.site.register(ServicesFrontPage, ServicesFrontPageAdmin)



class ServicesAdmin(admin.ModelAdmin):
    model = Services
    list_display = ['title', 'description_field']



admin.site.register(Services, ServicesAdmin)

