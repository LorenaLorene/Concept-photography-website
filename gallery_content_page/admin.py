from django.contrib import admin

from .models import GalleryFrontPage
from .models import GalleryImage




class GalleryFrontPageAdmin(admin.ModelAdmin):
    model = GalleryFrontPage
    list_display = ['main_title', 'description_field']


admin.site.register(GalleryFrontPage, GalleryFrontPageAdmin)



class GalleryImageAdmin(admin.ModelAdmin):
    model = GalleryImage
    list_display = ['image']



admin.site.register(GalleryImage, GalleryImageAdmin)
