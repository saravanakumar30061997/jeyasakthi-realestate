from django.shortcuts import render
from listings.choices import price_choices, bedroom_choices, locality_choices
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {"listings":listings,
               "price_choices":price_choices,
               "bedroom_choices":bedroom_choices,
               "locality_choices":locality_choices}
    return render(request,'pages/index.html', context=context)

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {"realtors":realtors, "mvp_realtors":mvp_realtors}
    return render(request,'pages/about.html', context=context)

