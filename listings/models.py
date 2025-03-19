from django.db import models
from datetime import datetime
from realtors.models import Realtor
from cloudinary.models import CloudinaryField
from django.urls import reverse



# Create your models here.
class Listing(models.Model):
    # Common choices
    CATEGORY_CHOICES = [
        ('real_estate', 'Real Estate'),
        ('jobs', 'Jobs'),
        ('services', 'Services'),
        ('business', 'Business'),
        ('vehicles', 'Vehicles'),
    ]

    LISTING_STATUS_CHOICES = [
        ('active', 'Active'),
        ('sold', 'Sold'),
        ('rented', 'Rented'),
        ('expired', 'Expired'),
    ]
    realtor = models.ForeignKey(Realtor,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='')
    status = models.CharField(max_length=10, choices=LISTING_STATUS_CHOICES, default='active')
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2,decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=7,decimal_places=1,blank=True, null=True)
    photo_main = CloudinaryField('photo_main')
    photo_1 = CloudinaryField('photo_1',null=True, blank=True)
    photo_2 = CloudinaryField('photo_2',null=True, blank=True)
    photo_3 = CloudinaryField('photo_3',null=True, blank=True)
    photo_4 = CloudinaryField('photo_4',null=True, blank=True)
    photo_5 = CloudinaryField('photo_5',null=True, blank=True)
    photo_6 = CloudinaryField('photo_6',null=True, blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    slug = models.SlugField(default="", null=False, unique=True, max_length=255)


    def get_absolute_url(self):
        return reverse('listing', args=[str(self.id)])  # Match this with your URL name


    def __str__(self):
        return self.title