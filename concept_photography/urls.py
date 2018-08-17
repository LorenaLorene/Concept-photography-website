"""concept_photography URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from . import views as homeViews
from about_us_page_content import views as aboutViews
from pricing_page import views as pricingViews
from services_page_content import views as servicesViews
from pay_online_page_content import views as payViews
from gallery_content_page import views as galleryViews
from faqs_page_content import views as faqsViews
from contact_information import views as contactViews
from gdpr_page_content import views as gdprViews
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^about', aboutViews.index),
    url(r'^pricing', pricingViews.index),
    url(r'^services', servicesViews.index),
    url(r'^pay', payViews.index),
    url(r'^gallery', galleryViews.index),
    url(r'^faqs', faqsViews.index),
    url(r'^contact', contactViews.index),
    url(r'^gdpr', gdprViews.index),
    url(r'^', homeViews.index),
]

urlpatterns += staticfiles_urlpatterns()