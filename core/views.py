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



def testimonialform(request):
    if request.method == "POST":
        name = request.POST.get("name")
        prof = request.POST.get("prof")
        prop_img = request.FILES.get("prop_img")
        disc = request.POST.get("disc")
        Testimonial.objects.create(
            name = name,
            prof = prof,
            prop_img = prop_img,
            disc  = disc
        )
        messages.success(request,"Thank you for giving your valuble feedback here")
        return redirect("home")
    return render(request,"form.html")

