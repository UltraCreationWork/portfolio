from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
from django.core.mail import send_mail

def home(request):

    data = {
        "services":Services.objects.all(),
        "members": Member.objects.all(),
        "testimonial": Testimonial.objects.all(),
        "address": Address.objects.all()[:1]
    }


    return render(request,"index.html",data)

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        Contact.objects.create(
                name = name,
                email = email,
                mobile_number = phone,
                subject = subject,
                message = message
        )

        send_mail(f"Name - {name}, Email - {email}, Phone Number - {phone}, Subject- {subject}",message,"urbanspacerealtors.rkl@gmail.com",["hr.rsdastudio@gmail.com"])
        messages.success( request,"Thank you for contacting us")
        return redirect("home")

    return redirect("home")





