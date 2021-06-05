from django.contrib import admin

from listings.models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'realtor', 'city', 'state', 'price', 'listing_date', 'published')
    list_editable = ('published',)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'city', 'price')
    list_filter = ('realtor', )
    list_per_page = 10

admin.site.register(Listing, ListingAdmin)
