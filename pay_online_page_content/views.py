from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from contact_information.models import ContactInfo
from pay_online_page_content.models import PayOnlineFrontPage
from pay_online_page_content.models import PayOnlineNote


def index(request):

    template = loader.get_template('pay.html')
    context = {'contactInfo': ContactInfo.objects.first(),
               'PayOnlineFrontPage': PayOnlineFrontPage.objects.first(),
               'PayOnlineNote': PayOnlineNote.objects.first()}

    return HttpResponse(template.render(context, request))
