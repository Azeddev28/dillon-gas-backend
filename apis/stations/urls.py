from django.urls import path

from apis.stations.bindings import inventory_list_view, item_details_view


urlpatterns = [
    path('inventory/', inventory_list_view, name='inventory'),
    path('inventory/item-details/<uuid:uuid>/', item_details_view, name='item-details'),
]
