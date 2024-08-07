from rest_framework.generics import ListAPIView

from apis.inventory.models import Item
from apis.inventory.serializers.item import ItemSerializer


class ItemListAPIView(ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        category = self.request.data.get('category')
        if not category:
            return Item.objects.all()
        return Item.objects.filter(category=category)
        
    def post(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)