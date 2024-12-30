from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'locality', 'realtor')  # Display locality
    list_display_links = ('id', 'title')
    list_filter = ('realtor', 'state')  # Enable filtering by locality (state)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25

    # Method to display locality instead of state
    def locality(self, obj):
        return obj.get_state_display()  # Retrieves the human-readable choice label
    locality.short_description = 'Locality'  # Rename column header in the list view

# Register your models here.
admin.site.register(Listing, ListingAdmin)
