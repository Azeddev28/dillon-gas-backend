from django.urls import path

from apis.inventory.bindings import item_list_view, category_list_view


urlpatterns = [
    path('items/', item_list_view, name='item-list'),
    path('categories/', category_list_view, name='category-list')
]
