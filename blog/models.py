from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = CloudinaryField('image',null=True, blank= True)
    description = models.TextField()
    date = models.DateField()
    slug = models.SlugField(default="", null=False,unique=True, max_length=255)

    def __str__(self):
        return self.title

