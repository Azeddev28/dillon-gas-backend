from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from apis.orders.models import Order
from apis.orders.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user).order_by('-created_at')
