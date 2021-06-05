from django.db import models
from datetime import datetime

class Realtor(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    join_date = models.DateTimeField(default=datetime.now,blank=True)
    is_mvp = models.BooleanField(default=False)
    image = models.ImageField(upload_to='realtors/%m/', default=None)

    def __str__(self):
        return self.name



