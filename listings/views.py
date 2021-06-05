from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from . import choices
from . import models

def listings(request):
    listings = models.Listing.objects.order_by('-listing_date')
    paginator = Paginator(listings, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'listings': page_obj,
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listings = models.Listing.objects.all()
    listing = get_object_or_404(listings, pk=listing_id)

    context = {
        'listing':listing,
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = models.Listing.objects.filter(published=True)

    #keyword_search
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = models.Listing.objects.filter(description__icontains=keywords, published=True)

    #city_search
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = models.Listing.objects.filter(city__iexact=city, published=True)

    #state_search
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = models.Listing.objects.filter(state__iexact=state, published=True)

    #bedroom_search
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = models.Listing.objects.filter(bedrooms__lte=bedrooms, published=True)

    #price_search
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = models.Listing.objects.filter(price__lte=price, published=True)

    context = {
        'listings':queryset_list,
        'state_choices':choices.state_choices,
        'bedroom_choices':choices.bedroom_choices,
        'price_choices':choices.price_choices,
        'user_value':request.GET,
    }
    return render(request, 'listings/search.html', context)
