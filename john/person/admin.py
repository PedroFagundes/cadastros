# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin

from input_mask.widgets import InputMask

from .models import CityRegion, City, CityNeighborhood, Person

admin.site.site_header = 'Professor John'


class PhoneInput(InputMask):
    mask = {'mask': '(99) 9999-9999'}


class MobilePhoneInput(InputMask):
    mask = {'mask': '(99) 99999-9999'}


class ZipCodeInput(InputMask):
    mask = {'mask': '99999-999'}


class DateInput(InputMask):
    mask = {'mask': '99/99/9999'}


class CPFInput(InputMask):
    mask = {'mask': '999.999.999-99'}


class PersonForm(forms.ModelForm):
    phone = forms.CharField(widget=PhoneInput, required=False)
    mobile_phone = forms.CharField(widget=MobilePhoneInput, required=False)
    zip_code = forms.CharField(widget=ZipCodeInput, required=False)
    birthdate = forms.CharField(widget=DateInput, required=False)
    cpf = forms.CharField(widget=CPFInput, required=False)
    class Meta:
        model = Person
        fields = ('__all__')


class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'neighborhood', 'get_region', 'city', 'phone', 'mobile_phone']
    list_filter = ['neighborhood__city_region', 'neighborhood']
    search_fields = ['name']
    form = PersonForm

    class Media:
        js = (
            'https://code.jquery.com/jquery-1.12.3.min.js',
        )

    def get_region(self, obj):
    	return obj.neighborhood.city_region
    get_region.short_description = u'Região'
    get_region.admin_order_field = 'city__region'

admin.site.register(Person, PersonAdmin)

# Register your models here.
