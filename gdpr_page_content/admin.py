from __future__ import unicode_literals
from django.contrib import admin
from .models import Gdpr


class GdprAdmin(admin.ModelAdmin):
    model = Gdpr
    list_display = ['main_title', 'description', 'small_title', 'gdpr_content', 'consent_link', 'stop_link']


admin.site.register(Gdpr, GdprAdmin)
