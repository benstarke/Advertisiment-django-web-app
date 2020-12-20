from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView
from .models import *

# Create your views here.


def servicesview(request,slug):
    object_list = myservices.objects.filter(slug=slug)
    context = {
        'obj':obj,
        'object_list':object_list
    }
    return render(request,'myadvert/services.html',context)


def home(request):
    slides = slider.objects.all()
    seen = index.objects.all()
    context = {
            'seen':seen,
            'slides':slides
    }
    return render(request,'myadvert/index.html',context)



def about(request):
    exp = workexperience.objects.all()
    pic = myprofile.objects.all()
    context = {
            'exp':exp,
            'pic':pic
    }
    return render(request,'myadvert/About.html',context)





def contact(request):
    return render(request,'myadvert/contact.html')


def services(request):
    obj = myservices.objects.all()
    context = {
        'obj':obj,
    }
    return render(request,'myadvert/services.html',context)