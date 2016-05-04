# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import CityRegion, City, CityNeighborhood, Person

admin.site.site_header = 'Professor John'


class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'neighborhood', 'get_region', 'city', 'phone', 'mobile_phone']
    list_filter = ['neighborhood__city_region', 'neighborhood']
    search_fields = ['name']

    def get_region(self, obj):
    	return obj.neighborhood.city_region
    get_region.short_description = u'Região'
    get_region.admin_order_field = 'city__region'

admin.site.register(Person, PersonAdmin)

# Register your models here.
