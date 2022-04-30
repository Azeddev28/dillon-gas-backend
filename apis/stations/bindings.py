from apis.stations.views.inventory import InventoryListAPIView, ItemDetailsRetrieveAPIView


inventory_list_view  = InventoryListAPIView.as_view()
item_details_view  = ItemDetailsRetrieveAPIView.as_view()
