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

    # Check if any filter is applied
    has_search_params = any(request.GET.get(param) for param in ['keywords', 'title', 'city', 'bedrooms', 'price'])

    if has_search_params:
        # Keywords (Description)
        if request.GET.get('keywords'):
            keywords = request.GET['keywords'].strip()
            if keywords:
                queryset_list = queryset_list.filter(description__icontains=keywords)

        # Title
        if request.GET.get('title'):
            title = request.GET['title'].strip()
            if title:
                queryset_list = queryset_list.filter(title__icontains=title)

        # City (Locality)
        if request.GET.get('city'):
            city = request.GET['city'].strip()
            if city and "All" not in city:  # Handle 'Locality (All)'
                queryset_list = queryset_list.filter(city__iexact=city)

        # Bedrooms
        if request.GET.get('bedrooms'):
            bedrooms = request.GET['bedrooms'].strip()
            if bedrooms.isdigit():
                queryset_list = queryset_list.filter(bedrooms=int(bedrooms))

        # Price
        if request.GET.get('price'):
            price = request.GET['price'].strip()
            if price.isdigit():
                queryset_list = queryset_list.filter(price__lte=int(price))

    

    context = {
        "price_choices": price_choices,
        "bedroom_choices": bedroom_choices,
        "locality_choices": locality_choices,
        "listings": queryset_list,
        "values": request.GET
    }
    return render(request, 'listings/search.html', context)

