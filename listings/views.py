from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .choices import price_choices, bedroom_choices, locality_choices


# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings':paged_listings
    }
    return render(request,'listings/listings.html',context=context)

def listing(request,slug):
    listing = get_object_or_404(Listing,slug=slug)
    context = {
        "listing":listing
    }

    return render(request,'listings/listing.html', context)

def search(request):

    queryset_list = Listing.objects.order_by('-list_date').filter(is_published=True)
    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    #title
    if 'title' in request.GET:
        keywords = request.GET['title'].strip()  # Remove leading/trailing spaces
        if keywords:
            queryset_list = queryset_list.filter(title__icontains=keywords)
    #locality_choices
    city = request.GET.get('city', None)
    if city and city != "Locality (All)":
        queryset_list = queryset_list.filter(city__iexact=city)

    #bedrooms
    if 'bedrooms' in request.GET:
        keywords = request.GET['bedrooms']  # Remove leading/trailing spaces
        if keywords:
            queryset_list = queryset_list.filter(bedrooms__lte=keywords)
    #price
    if 'price' in request.GET:
        keywords = request.GET['price']  # Remove leading/trailing spaces
        if keywords:
            queryset_list = queryset_list.filter(price__lte=keywords)

    context = {
        "price_choices":price_choices,
        "bedroom_choices":bedroom_choices,
        "locality_choices":locality_choices,
        "listings":queryset_list,
        "values":request.GET
    }
    return render(request,'listings/search.html', context=context)
