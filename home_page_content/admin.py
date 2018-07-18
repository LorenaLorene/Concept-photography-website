from django.contrib import admin


from .models import HomeFrontPage
from .models import CompanyVision
from .models import ShootCount
from .models import PhotographersCount
from .models import OurService





class HomeFrontPageAdmin(admin.ModelAdmin):
    model = HomeFrontPage
    list_display = ['main_title', 'small_title']


admin.site.register(HomeFrontPage, HomeFrontPageAdmin)



class CompanyVisionAdmin(admin.ModelAdmin):
    model = CompanyVision
    list_display = ['title', 'vision']



admin.site.register(CompanyVision, CompanyVisionAdmin)


class ShootCountAdmin(admin.ModelAdmin):
    model = ShootCount
    list_display = ['count_title', 'description_field']


admin.site.register(ShootCount, ShootCountAdmin)


class PhotographersCountAdmin(admin.ModelAdmin):
    model = PhotographersCount
    list_display = ['count_title', 'description_field']


admin.site.register(PhotographersCount, PhotographersCountAdmin)



class OurServiceAdmin(admin.ModelAdmin):
    model = OurService
    list_display = ['main_title', 'title', 'description_field']



admin.site.register(OurService, OurServiceAdmin)