from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Blog

class BlogSitemap(Sitemap):
    changefreq = "weekly"  # How often the content changes
    priority = 0.8  # Priority of this URL in the sitemap (1.0 is highest)

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.date  # Assuming 'date' is your last modified field

    def location(self, obj):
        return reverse('blog:detail', kwargs={'slug': obj.slug})  # Corrected to use 'slug'
