from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField()
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=2, decimal_places=1)
    listing_date = models.DateTimeField(default=datetime.now, blank=True)
    published = models.BooleanField(default=True)
    main_image = models.ImageField(upload_to='images/%m/')
    image_1 = models.ImageField(upload_to='images/%m/', blank=True)
    image_2 = models.ImageField(upload_to='images/%m/', blank=True)
    image_3 = models.ImageField(upload_to='images/%m/', blank=True)
    image_4 = models.ImageField(upload_to='images/%m/', blank=True)
    image_5 = models.ImageField(upload_to='images/%m/', blank=True)
    image_6 = models.ImageField(upload_to='images/%m/', blank=True)

    def __str__(self):
        return self.title



