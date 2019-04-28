from django.conf import settings
from django.db import models
from django.utils import timezone



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Newletter(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name | self.email


class FreeQuote(models.Model):
    """docstring for FreeQuote"""
    serviceAvailable = (
        ('nw', 'New Pavement Installation'), 
        ('cp', 'Cleaning pavements'), 
        ('pm', 'Pavement Maintenance'),
        ('tc', 'Tiles cleaning'),
        ('tm', 'Tiles Maintenance'),
        ('nt', 'New Tiles Installation'),
        ('oe', 'Other services'),
    )

    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    cell_number = models.IntegerField(blank=True)
    address = models.CharField(max_length=200, blank=True)
    service_req = models.CharField(max_length=4, choices=serviceAvailable )
    additional_info = models.TextField(blank=True)
    location = models.CharField(max_length=200)
     
    def __str__(self):
        return self.name   


class Contact(models.Model):
   name = models.CharField(max_length=200)
   email = models.EmailField(max_length=200)
   phone = models.CharField(max_length=15)
   subject = models.CharField(max_length=200)
   message = models.TextField()

   def __str__(self):
        return self.name
# Create your models here.

