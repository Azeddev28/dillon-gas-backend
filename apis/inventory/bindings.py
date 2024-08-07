from apis.inventory.views.item import ItemListAPIView
from apis.inventory.views.category import CategoryListAPIView


item_list_view = ItemListAPIView.as_view()
category_list_view = CategoryListAPIView.as_view()
