from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from contact_information.models import ContactInfo
from about_us_page_content.models import AboutUsFrontPage
from about_us_page_content.models import Testimonial
from about_us_page_content.models import MeetOurTeam
from about_us_page_content.models import OurTeam
from about_us_page_content.models import CustomerServiceTeam



def index(request):
    template = loader.get_template('about.html')
    context = {'contactInfo': ContactInfo.objects.first(),
               'aboutUs': AboutUsFrontPage.objects.first(),
               'Testimonials': Testimonial.objects.all(),
               'MeetOurTeamTitle': MeetOurTeam.objects.first(),
               'OurTeams': OurTeam.objects.all(),
               'CustomerService': CustomerServiceTeam.objects.first()}

    return HttpResponse(template.render(context, request))
