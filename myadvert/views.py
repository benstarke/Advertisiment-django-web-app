from django.shortcuts import render
from django.views.generic import ListView
from .models import *
# Create your views here.


def home(request):
    slides = slider.objects.all()
    seen = index.objects.all()
    context = {
            'seen':seen,
            'slides':slides
    }
    return render(request,'myadvert/index.html',{})



def about(request):
    exp = workexperience.objects.all()
    pic = myprofile.objects.all()
    context = {
            'exp':exp,
            'pic':pic
    }
    return render(request,'myadvert/About.html',{})

def services(request):
    service = myservices.objects.all()
    return render(request,'myadvert/services.html',{'service':service})

def contact(request):
    return render(request,'myadvert/contact.html')