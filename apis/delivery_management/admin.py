from copy import copy
from django import forms
from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.contrib.auth import get_user_model

from cities_light.models import City, Region
from cities_light.abstract_models import to_search

from apis.delivery_management.forms import DGCityForm, DGRegionForm
from apis.delivery_management.models import DeliveryInfo, OrderDelivery

User = get_user_model()


class RegionAdmin(admin.ModelAdmin):
    """
    ModelAdmin for Region.
    """
    list_filter = (
        'country__continent',
        'country',
    )
    search_fields = (
        'name',
        'name_ascii',
        'geoname_id',
    )
    list_display = (
        'name',
        'country',
        'geoname_id',
        'delivery_enabled'
    )
    form = DGRegionForm


class CityChangeList(ChangeList):
    def get_queryset(self, request):
        if 'q' in list(request.GET.keys()):
            request.GET = copy(request.GET)
            request.GET['q'] = to_search(request.GET['q'])
        return super().get_queryset(request)


class CityAdmin(admin.ModelAdmin):
    """
    ModelAdmin for City.
    """
    raw_id_fields = ["subregion", "region"]
    list_display = (
        'name',
        'subregion',
        'region',
        'country',
        'geoname_id',
        'timezone',
        'delivery_enabled'
    )
    search_fields = (
        'search_names',
        'geoname_id',
        'timezone'
    )
    list_filter = (
        'country__continent',
        'country',
        'timezone'
    )
    form = DGCityForm

    def get_changelist(self, request, **kwargs):
        return CityChangeList


class DeliveryInfoAdmin(admin.ModelAdmin):
    list_display = ['city', 'state', 'delivery_cost', 'min_delivery_time', 'max_delivery_time']

    class Meta:
        model = DeliveryInfo

    def get_form(self, request, obj = ..., change= ..., **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['state'] = forms.ModelChoiceField(Region.objects.filter(delivery_enabled=True))
        form.base_fields['city'] = forms.ModelChoiceField(City.objects.filter(delivery_enabled=True))
        return form


class OrderDeliveryAdmin(admin.ModelAdmin):
    list_display = ['order', 'delivery_agent', 'pickup_datetime', 'delivery_datetime']

    class Meta:
        model = OrderDelivery

    def get_form(self, request, obj = ..., change: bool = ..., **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['delivery_agent'] = forms.ModelChoiceField(User.objects.filter(role='delivery_agent'))
        return form

admin.site.unregister(City)
admin.site.register(City, CityAdmin)
admin.site.unregister(Region)
admin.site.register(Region, RegionAdmin)
admin.site.register(DeliveryInfo, DeliveryInfoAdmin)
admin.site.register(OrderDelivery, OrderDeliveryAdmin)
