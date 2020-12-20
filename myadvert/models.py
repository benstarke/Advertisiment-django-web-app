from django.db import models
from django.utils import timezone
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Adjust,ResizeToFit
from pilkit.processors import Thumbnail

# Create your models here.
#index
#about
#services
#slider



#homepage models
class index(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    img = models.ImageField(upload_to='homepage')
    image = ImageSpecField(source='img',processors=[ResizeToFill(200, 100)],
            format='PNG', options={'quality': 90})

    class Meta:
        verbose_name_plural = 'index'

    def __str__(self):
        return self.title

#slider model
class slider(models.Model):
    title = models.CharField(max_length=255,default=None)
    description = models.TextField(default=None)
    img = models.ImageField(upload_to='homepage')
    image = ImageSpecField(source='img',processors=[ResizeToFill(1000, 1000)],
            format='PNG', options={'quality': 90})

    class Meta:
        verbose_name_plural = 'slider'



#about page models
class myprofile(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    img = models.ImageField(upload_to='profile')
    image = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
            ResizeToFill(374, 512)], source='img',
            format='PNG', options={'quality': 100})

    class Meta:
        verbose_name_plural = 'myprofile'

    def __str__(self):
        return self.title


class workexperience(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    img = models.ImageField(upload_to='myworkexperience')
    image = ImageSpecField([
            ResizeToFill(150, 150)], source='img',
            format='PNG', options={'quality': 100})

    class Meta:
        verbose_name_plural = 'workexperience'
    
    def __str__(self):
        return self.title


#service page models
services = [
    ('Fittings','Fittings'),
     ('Wiring','Wiring'),
      ('Tiles','Tiles'),
       ('Ceilings','Ceilings'),
        ('Plumbing','Plumbing'),
         ('Painting','Painting'),
]

class myservices(models.Model):
    slug = models.SlugField(max_length=15,choices=services)
    description = models.TextField()
    img = models.ImageField(upload_to='services')
    image = ImageSpecField([ResizeToFill(200, 100)], source='img',
            format='PNG', options={'quality': 100})
    
    class Meta:
        verbose_name_plural = "myservices"
    
    def __str__(self):
        return self.slug
