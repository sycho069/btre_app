from django.contrib import admin
from realtors.models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'join_date', 'is_mvp')
    list_display_links = ('id', 'name')
    list_editable = ('is_mvp', )


admin.site.register(Realtor, RealtorAdmin)
