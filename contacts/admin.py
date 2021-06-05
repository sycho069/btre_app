from django.contrib import admin

from . import models

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'property', 'name', 'email', 'realtor_name', 'contact_date']
    list_display_links = ['id', 'property']
    list_per_page = 10

admin.site.register(models.Contact, ContactAdmin)
