from django.contrib import admin
from .models import PayOnlineFrontPage
from .models import PayOnlineNote


class PayOnlineFrontPageAdmin(admin.ModelAdmin):
    model = PayOnlineFrontPage
    list_display = ['main_title', 'title', 'description']


admin.site.register(PayOnlineFrontPage, PayOnlineFrontPageAdmin)


class PayOnlineNoteAdmin(admin.ModelAdmin):
    model = PayOnlineNote
    list_display = ['please_note']


admin.site.register(PayOnlineNote, PayOnlineNoteAdmin)
