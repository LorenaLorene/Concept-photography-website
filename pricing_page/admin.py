from django.contrib import admin



from .models import PricingFrontPage
from .models import Pricing





class PricingFrontPageAdmin(admin.ModelAdmin):
    model = PricingFrontPage
    list_display = ['main_title', 'description']


admin.site.register(PricingFrontPage, PricingFrontPageAdmin)



class PricingAdmin(admin.ModelAdmin):
    model = Pricing
    list_display = ['digital_prices', 'canvas_prices']



admin.site.register(Pricing, PricingAdmin)
