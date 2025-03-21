from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('search/', views.search, name='search'),

    # Optional: Redirect old ID-based URLs if they existed
    path('<int:id>/', views.redirect_to_slug, name='listing-redirect'),

    # New slug-based listing URL
    path('<slug:slug>/', views.listing, name='listing'),
]
