"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar
from django.contrib.sitemaps.views import sitemap
from listings.sitemaps import ListingSitemap
from pages.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap
from django.views.generic.base import TemplateView



sitemaps = {
    "static": StaticViewSitemap(),
    "listings": ListingSitemap(),
    'blog': BlogSitemap(),
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pages.urls')),
    path('listings/',include('listings.urls')),
    path('accounts/',include('accounts.urls')),
    path('contacts/',include('contacts.urls')),
    path('blogs/',include('blog.urls')),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path('googleef77926a2a0da1fa.html', TemplateView.as_view(template_name="googleef77926a2a0da1fa.html", content_type="text/html")),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
