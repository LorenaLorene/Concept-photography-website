from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from contact_information.models import ContactInfo
from gallery_content_page.models import GalleryFrontPage
from gallery_content_page.models import GalleryImage


def index(request):
    template = loader.get_template('gallery.html')
    context = {'contactInfo': ContactInfo.objects.first(),
               'GalleryFrontPage': GalleryFrontPage.objects.first(),
               'GalleryImage': GalleryImage.objects.all()}

    return HttpResponse(template.render(context, request))
