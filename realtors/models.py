from django.db import models
from datetime import datetime
from cloudinary.models import CloudinaryField


# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=255)
    photo = CloudinaryField('photo')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name