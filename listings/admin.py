from django.contrib import admin
from .models import Listing

# Unregister Listing if already registered (prevents AlreadyRegistered error)
try:
    admin.site.unregister(Listing)
except admin.sites.NotRegistered:
    pass

# Register Listing with custom admin
@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'city', 'state', 'price', 'is_published', 'list_date')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', 'city', 'state', 'is_published')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'city', 'state', 'zipcode')
    ordering = ('-list_date',)

    # Fields to display in the add/edit form
    fields = (
        'title',
        'slug',
        'description',
        'price',
        'bedrooms',
        'bathrooms',
        'garage',
        'sqft',
        'lot_size',
        'city',
        'state',
        'zipcode',
        'latitude',   # optional field
        'longitude',  # optional field
        'photo_main',
        'photo_1',
        'photo_2',
        'photo_3',
        'photo_4',
        'photo_5',
        'photo_6',
        'is_published',
        'list_date',
        'realtor',
    )
