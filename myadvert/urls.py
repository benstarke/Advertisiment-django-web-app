from django.urls import path
#from .import views
#from myadvert.views import *
from myadvert import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about-my-experience-and-work/',views.about,name='about'),
    path('how-to-get-me/',views.contact,name='contact'),
    path('what-i-offer-to-my-clients/',views.services,name='services'),
]