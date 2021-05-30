from django.urls import path,include
from .views import home,contact,testimonialform
from django.contrib.sitemaps.views import sitemap
from .sitemaps import *
from django.views.generic.base import TemplateView

sitemaps = {
    'static':Staticsitemaps,
}




urlpatterns = [
    path("",home,name="home"),
    path("contact/",contact,name="contact"),
    path("form/",testimonialform,name="form"),
    path('sitemap.xml/',sitemap,{'sitemaps':sitemaps}),
    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain"))



]