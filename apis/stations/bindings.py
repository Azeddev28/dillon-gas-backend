from apis.stations.views.inventory import (InventoryListAPIView, ItemDetailsRetrieveAPIView,
                                           ItemQualificationsListAPIView)


inventory_list_view = InventoryListAPIView.as_view()
item_details_view = ItemDetailsRetrieveAPIView.as_view()
item_qualifications_view = ItemQualificationsListAPIView.as_view()
