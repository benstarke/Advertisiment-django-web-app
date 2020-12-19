from django.urls import path
from .import views
from myadvert.views import *
#from myadvert import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about-my-experience-and-work/',views.about,name='about'),
    path('how-to-get-me/',views.contact,name='contact'),
    path('services/',views.services,name='services'),
    path('services/<slug>/',views.servicesview,name='servicesview'),
    #path('hasd/',views.services,name='services'),
]