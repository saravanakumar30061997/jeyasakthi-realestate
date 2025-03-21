from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.all_blogs, name='all_blogs'),

    # Redirect old ID-based URLs to slug URLs
    path("<int:id>/", views.redirect_to_slug, name='blog-redirect'),

    # New slug-based URL for blog details
    path("<slug:slug>/", views.detail, name='detail'),
]
