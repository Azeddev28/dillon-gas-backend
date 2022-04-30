from rest_framework.generics import ListAPIView
from apis.stations.models import StationInventory

from apis.stations.serializers.inventory import InventoryListSerializer


class InventoryListAPIView(ListAPIView):
    serializer_class = InventoryListSerializer

    def get_queryset(self):
        category = self.request.data.get('category')
        if not category:
            return StationInventory.objects.all()
        return StationInventory.objects.filter(item__category=category)
        
    def post(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
