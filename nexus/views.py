from django.shortcuts import render,redirect
from django .http import HttpResponse
from .models import Enquiry
from django.contrib import messages

# Create your views here.
def home_view(request):
    return render(request,"home.html")

def service_view(request):
    return render(request,"service.html")

def gallery_view(request):
    return render(request,"gallery.html")

def contact_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        message = request.POST.get("message")
        
       
        Enquiry.objects.create(
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            message=message
        )
        
        messages.success(request, "Your enquiry has been submitted successfully..!")
        return redirect("enquiry")  
    return render(request, "contact.html")