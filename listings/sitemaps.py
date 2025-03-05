from django.contrib.sitemaps import Sitemap
from .models import Listing

class ListingSitemap(Sitemap):
    changefreq = "weekly"  # You can set this based on your preference
    priority = 0.8  # Higher means more important pages for indexing

    def items(self):
        return Listing.objects.all()  # Fetch all listings

    def lastmod(self, obj):
        return obj.updated_at  # Uses updated_at field to inform Google about modifications
