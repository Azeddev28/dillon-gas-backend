from rest_framework.generics import ListAPIView, RetrieveAPIView
from apis.inventory.models import ItemQualification
from apis.stations.models import StationInventoryItem

from apis.stations.serializers.inventory import InventoryDetailSerializer, InventoryListSerializer, ItemQualificationSerializer


class InventoryListAPIView(ListAPIView):
    serializer_class = InventoryListSerializer

    def get_queryset(self):
        category = self.request.data.get('category')
        if not category:
            return StationInventoryItem.objects.all()
        return StationInventoryItem.objects.filter(item__category=category)
        
    def post(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)


class ItemDetailsRetrieveAPIView(RetrieveAPIView):
    serializer_class = InventoryDetailSerializer
    lookup_field = 'uuid'
    queryset = StationInventoryItem.objects.all()


class ItemQualificationsListAPIView(ListAPIView):
    serializer_class = ItemQualificationSerializer

    def get_queryset(self):
        item_uuid = self.request.data.get('item_uuid')
        return ItemQualification.objects.filter(item__uuid=item_uuid)

    def post(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
