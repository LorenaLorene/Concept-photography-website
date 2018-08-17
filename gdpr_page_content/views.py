from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from contact_information.models import ContactInfo
from gdpr_page_content.models import Gdpr


def index(request):

    template = loader.get_template('gdpr.html')
    context = {'contactInfo': ContactInfo.objects.first(),
               'Gdpr': Gdpr.objects.first()}

    return HttpResponse(template.render(context, request))
