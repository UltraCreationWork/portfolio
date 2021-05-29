from re import VERBOSE
from django.db import models
from django.db.models.base import ModelBase
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

class Member(models.Model):
    name                =   models.CharField(max_length=30,verbose_name="Name")
    prof                =   models.CharField(max_length=20,verbose_name="Profession")
    img                 =   models.ImageField(upload_to="media",verbose_name="Profile Picture")
    content             =   RichTextField(blank=True,verbose_name="About Me")
    join_date           =   models.DateField(auto_created=True)

    class Meta:
        ordering = ["pk"]


    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100,verbose_name="Name")
    email = models.EmailField(verbose_name="Email",blank=True)
    mobile_number = PhoneNumberField(null=True, validators=[RegexValidator(r'^\d{3}-\d{3}-\d{4}$')])
    subject = models.CharField(max_length=200)
    message = RichTextField()
    date    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-date"]


class Address(models.Model):
    location_line_1 = models.CharField(max_length=200,verbose_name="Address Line 1")
    location_line_2 = models.CharField(max_length=200,verbose_name="Address Line 2")
    location_line_3 = models.CharField(max_length=200,verbose_name="Address Line 3",blank=True)
    email   = models.EmailField(verbose_name="Email")
    mobile_number = PhoneNumberField(verbose_name="Mobile Number")

    def __str__(self):
        return self.email
    
    class Meta:
        ordering = ["pk"]


class Services(models.Model):
    symbol = models.CharField(max_length=255,blank=True,verbose_name="Icon")
    name = models.CharField(max_length=500,verbose_name="Name")
    dics = RichTextField(verbose_name="Content")
    number = models.PositiveIntegerField(verbose_name="Number")

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['number']

class Testimonial(models.Model):
    name                =       models.CharField(max_length=255,verbose_name="Name")
    prop_img            =       models.ImageField(upload_to='realestate/testimonial',verbose_name="Project Image")
    prof                =       models.CharField(max_length=100,verbose_name="Profession",blank=True)
    disc                =       models.CharField(max_length=500,verbose_name="Review")


    def __str__(self):
        return self.name
