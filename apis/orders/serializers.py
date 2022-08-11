from curses import keyname
from django.contrib.auth import get_user_model

from rest_framework import serializers

from apis.stations.models import StationInventoryItem
from apis.inventory.models import Item
from apis.orders.models import Order, OrderItem

User = get_user_model()


class OrderItemSerializer(serializers.ModelSerializer):
    item = serializers.SlugRelatedField(slug_field='uuid', queryset=StationInventoryItem.objects.all())

    class Meta:
        model = OrderItem
        fields = ['item', 'uuid', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(), 
        queryset=User.objects.all(),
        slug_field='email'
    )
    order_items = OrderItemSerializer(many=True)
    order_status = serializers.CharField(source='get_order_status_display', required=False)
    payment_status = serializers.CharField(source='get_payment_status_display', required=False)

    class Meta:
        model = Order
        exclude = ['id', 'is_active']

    def _create_order_items(self, order_items_data, order):
        order_items = [OrderItem(**order_item_data, order=order) for order_item_data in order_items_data]
        order_items = OrderItem.objects.bulk_create(order_items)
        return order_items

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)
        self._create_order_items(order_items_data, order)
        return order
