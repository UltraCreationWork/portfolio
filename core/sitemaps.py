from django.contrib import sitemaps
from django.contrib.sitemaps import Sitemap
from .models import *
from django.shortcuts import reverse

# class MemberSitemap(Sitemap):
#     def items(self):
#         return Member.objects.all()

# class TestimonialSitemaps(Sitemap):
#     def items(self):
#         return Testimonial.objects.all()

# class AddressSitemap(Sitemap):
#     def items(self):
#         return Address.objects.all()

# class ServiceSitemap(Sitemap):
#     def items(self):
#         return Services.objects.all()

class Staticsitemaps(Sitemap):
    
    def items(self):
        return ['home','contact','form']

    def location(self,item):
        return reverse(item)
    
