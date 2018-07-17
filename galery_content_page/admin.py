from django.contrib import admin

from .models import GaleryFrontPage
from .models import GaleryImages




class GaleryFrontPageAdmin(admin.ModelAdmin):
    model = GaleryFrontPage
    list_display = ['main_title', 'description_field']


admin.site.register(GaleryFrontPage, GaleryFrontPageAdmin)



class GaleryImagesAdmin(admin.ModelAdmin):
    model = GaleryImages
    list_display = ['image']



admin.site.register(GaleryImages, GaleryImagesAdmin)
