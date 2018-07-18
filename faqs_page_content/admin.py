from __future__ import unicode_literals
from django.contrib import admin
from .models import PhotographyFaq


class PhotographyFaqAdmin(admin.ModelAdmin):
    model = PhotographyFaq
    list_display = ['title', 'faq']


admin.site.register(PhotographyFaq, PhotographyFaqAdmin)
