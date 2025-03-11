from django.db import models
from listings.models import Listing  

class Contact(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="contacts")  
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(auto_now_add=True)  
    user_id = models.IntegerField(null=True, blank=True)  

    def __str__(self):
        return f"Inquiry by {self.name} for {self.listing.title}"
