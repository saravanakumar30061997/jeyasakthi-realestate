from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='listings'),
    path('search/',views.search,name='search'),
    path('<slug:slug>/',views.listing,name='listing'),  
]
