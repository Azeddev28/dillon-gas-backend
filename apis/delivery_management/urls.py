from django.urls import path

from apis.delivery_management.bindings import (delivery_info_retrieve_view,
                                               city_list_view, region_list_view)


urlpatterns = [
    path('delivery-info/', delivery_info_retrieve_view, name='delivery-info'),
    path('regions/', region_list_view, name='delivery-info'),
    path('cities/', city_list_view, name='delivery-info'),
]
