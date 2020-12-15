from django.contrib import admin
from myadvert.models import *
# Register your models here.

class indexAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


class myprofileAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

class workexperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


class myservicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


admin.site.site_header = 'Bonface'


admin.site.register(index,indexAdmin)
admin.site.register(slider)
admin.site.register(myprofile,myprofileAdmin)
admin.site.register(workexperience,workexperienceAdmin)
admin.site.register(myservices,myservicesAdmin)