from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from apis.orders.models import Order
from apis.orders.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]
