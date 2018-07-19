from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render



def index(request):
    template = loader.get_template('home.html')
    context = {'main_title': 'Preschool and Nursery specialists', 'small_title': 'Rethink Nursery/Preschool photography', 'phone_number': '000000'}
    return HttpResponse(template.render(context, request))