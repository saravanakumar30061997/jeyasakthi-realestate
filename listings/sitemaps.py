from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Listing

class ListingSitemap(Sitemap):
    changefreq = "weekly"  # You can set this based on your preference
    priority = 0.8  # Higher means more important pages for indexing

    def items(self):
        return Listing.objects.filter(is_published=True)  # Fetch only published listings

    def lastmod(self, obj):
        return obj.updated_at  # Use updated_at to inform Google about modifications

    def location(self, obj):
        return reverse('listing', kwargs={'slug': obj.slug})  # Use 'slug' instead of 'id'
