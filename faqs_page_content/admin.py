from __future__ import unicode_literals

from django.contrib import admin

from .models import PhotographyFaqs


class PhotographyFaqsAdmin(admin.ModelAdmin):
    model = PhotographyFaqs
    list_display = ['title', 'faqs']


admin.site.register(PhotographyFaqs, PhotographyFaqsAdmin)
