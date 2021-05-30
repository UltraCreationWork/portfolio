from django.urls import path,include
from .views import home,contact,testimonialform

urlpatterns = [
    path("",home,name="home"),
    path("contact/",contact,name="contact"),
    path("form/",testimonialform,name="form")


]