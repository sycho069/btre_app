from django.shortcuts import render

from listings.models import Listing
from realtors import models
from listings import choices

def index(request):
    listings = Listing.objects.order_by('-listing_date')[:3]

    context = {
        'listings':listings,
        'state_choices':choices.state_choices,
        'bedroom_choices':choices.bedroom_choices,
        'price_choices':choices.price_choices,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    realtors = models.Realtor.objects.all()
    is_mvp = models.Realtor.objects.filter(is_mvp=True)

    context = {
        'realtors':realtors,
        'is_mvp':is_mvp,
    }
    return render(request, 'pages/about.html', context)