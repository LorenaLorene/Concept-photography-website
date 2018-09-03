from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from home_page_content.models import CompanyVision
from home_page_content.models import ShootCount
from home_page_content.models import PhotographersCount
from home_page_content.models import OurService
from contact_information.models import ContactInfo
from home_page_content.models import ClickToPayLink



def OurServiceByIndex(allOurServices, Index):
    if Index < len(allOurServices):
        return allOurServices[Index]
    else:
        return False

def index(request):
    allOurServices = OurService.objects.all()
    firstService = OurServiceByIndex(allOurServices, 0)
    secondService = OurServiceByIndex(allOurServices, 1)
    thirdService = OurServiceByIndex(allOurServices, 2)

    shouldShowCompanyVision = len(CompanyVision.objects.all()) >= 1


    template = loader.get_template('home.html')
    context = { 'main_title': 'Preschool and Nursery specialists',
                'small_title': 'Rethink Nursery/Preschool photography',
                'ClickToPayLink': ClickToPayLink.objects.first(),
                'CompanyVisions': CompanyVision.objects.all(),
                'shouldShowCompanyVision': shouldShowCompanyVision,
                'ShootCount': ShootCount.objects.first(),
                'PhotographersCount': PhotographersCount.objects.first(),
                'OurServices': OurService.objects.all(),
                'firstService': firstService,
                'secondService': secondService,
                'thirdService': thirdService,
                'contactInfo' : ContactInfo.objects.first()}
    return HttpResponse(template.render(context, request))