from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.7  # Higher means more important for search engines
    changefreq = "monthly"  # How often the page is likely to change

    def items(self):
        return ["index", "about"]  # Add all static page names

    def location(self, item):
        return reverse(item)
