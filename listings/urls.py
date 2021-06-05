from django.urls import path

from . import views

urlpatterns = [
    path('listings/', views.listings, name='listings_page'),
    path('<int:listing_id>', views.listing, name='listing_page'),
    path('search/', views.search, name='search_page')
]