from apis.delivery_management.views import (CityListView, DeliveryInfoRetreieveView,
                                            RegionListView)


delivery_info_retrieve_view = DeliveryInfoRetreieveView.as_view()
city_list_view = CityListView.as_view()
region_list_view = RegionListView.as_view()
