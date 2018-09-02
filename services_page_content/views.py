from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from contact_information.models import ContactInfo
from services_page_content.models import ServicesFrontPage
from services_page_content.models import Service


def index(request):

    shouldShowServices = len(Service.objects.all()) >= 1

    template = loader.get_template('services.html')
    context = {'contactInfo': ContactInfo.objects.first(),
               'ServicesFrontPage': ServicesFrontPage.objects.first(),
               'Service': Service.objects.all(),
               'shouldShowServices': shouldShowServices}

    return HttpResponse(template.render(context, request))
