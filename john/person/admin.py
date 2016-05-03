# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import CityRegion, City, CityNeighborhood, Person


class PersonAdmin(admin.ModelAdmin):
    display_list = ['name', 'address', 'neighborhood', 'neighborhood.city_region', 'city']

admin.site.register(Person, PersonAdmin)

# Register your models here.
