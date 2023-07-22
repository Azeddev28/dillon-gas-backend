from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apis.orders.models import Order
from apis.orders.serializers import DeliveryAgentOrderUpdateSerializer, OrderSerializer, OrderStatusSerializer
import logging
logger = logging.getLogger('daphne')


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'uuid'

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user).order_by('-created_at')


class FetchOrderStatusAPIView(RetrieveAPIView):
    lookup_field = 'uuid'
    serializer_class = OrderStatusSerializer

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user).order_by('-created_at')


class DeliveryAgentOrderUpdate(UpdateAPIView):
    serializer_class = DeliveryAgentOrderUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        logger.info(self.request.user.agent_orders.all())
        active_delivery = self.request.user.agent_orders.filter(order_active=True).first()
        return active_delivery.order
