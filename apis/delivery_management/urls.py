from django.urls import path

from apis.delivery_management.bindings import delivery_info_retrieve_view


urlpatterns = [
    path('delivery-info/', delivery_info_retrieve_view, name='delivery-info')
]
