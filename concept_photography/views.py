from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from home_page_content.models import CompanyVision
from home_page_content.models import ShootCount
from home_page_content.models import PhotographersCount
from home_page_content.models import OurService
from contact_information.models import ContactInfo


def index(request):


    allOurServices = OurService.objects.all()
    firstService = allOurServices[0]
    secondService = allOurServices[1]
    thirdService = allOurServices[2]


    template = loader.get_template('home.html')
    context = { 'main_title': 'Preschool and Nursery specialists',
                'small_title': 'Rethink Nursery/Preschool photography',
                'CompanyVisions': CompanyVision.objects.all(),
                'ShootCount': ShootCount.objects.first(),
                'PhotographersCount': PhotographersCount.objects.first(),
                'OurServices': OurService.objects.all(),
                'firstService': firstService,
                'secondService': secondService,
                'thirdService': thirdService,
                'contactInfo' : ContactInfo.objects.first()}
    return HttpResponse(template.render(context, request))