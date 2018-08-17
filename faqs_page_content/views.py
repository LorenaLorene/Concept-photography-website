from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from contact_information.models import ContactInfo
from faqs_page_content.models import PhotographyFaq


def index(request):

    template = loader.get_template('faqs.html')
    context = {'contactInfo': ContactInfo.objects.first(),
               'PhotographyFaqs': PhotographyFaq.objects.all()}

    return HttpResponse(template.render(context, request))
