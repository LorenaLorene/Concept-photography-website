from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from contact_information.models import ContactInfo


def index(request):
    template = loader.get_template('pricing.html')
    context = {'contactInfo': ContactInfo.objects.first()}

    return HttpResponse(template.render(context, request))
