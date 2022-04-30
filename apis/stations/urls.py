from django.urls import path

from apis.stations.bindings import inventory_list_view


urlpatterns = [
    path('inventory/', inventory_list_view, name='inventory'),
]
