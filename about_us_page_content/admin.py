from __future__ import unicode_literals
from django.contrib import admin
from .models import AboutUsFrontPage
from .models import MeetOurTeam
from .models import OurTeam
from .models import CustomerServiceTeam


class AboutUsFrontPageAdmin(admin.ModelAdmin):
    model = AboutUsFrontPage
    list_display = ['main_title', 'title', 'description_field', 'office_hours', 'testimonials']


admin.site.register(AboutUsFrontPage, AboutUsFrontPageAdmin)


class MeetOurTeamAdmin(admin.ModelAdmin):
    model = MeetOurTeam
    list_display = ['title']


admin.site.register(MeetOurTeam, MeetOurTeamAdmin)


class OurTeamAdmin(admin.ModelAdmin):
    model = OurTeam
    list_display = ['occupation']


admin.site.register(OurTeam, OurTeamAdmin)


class CustomerServiceTeamAdmin(admin.ModelAdmin):
    model = CustomerServiceTeam
    list_display = ['main_title', 'description_field']


admin.site.register(CustomerServiceTeam, CustomerServiceTeamAdmin)
