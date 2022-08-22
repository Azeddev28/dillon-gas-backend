from django.contrib.auth import get_user_model

from rest_framework import serializers

from apis.orders.choices import OrderStatus
from apis.orders.utils.validation_messages import OUT_OF_STOCK_MESSAGE

from .serializer_fields.payment_status import PaymentStatusField

from .serializer_fields.order_status import OrderStatusField
from .serializer_fields.payment_method import PaymentMethodField

from apis.stations.models import StationInventoryItem
from apis.inventory.models import Item
from apis.orders.models import Order, OrderItem

User = get_user_model()


class OrderItemSerializer(serializers.ModelSerializer):
    item = serializers.SlugRelatedField(slug_field='uuid', queryset=StationInventoryItem.objects.all())

    class Meta:
        model = OrderItem
        fields = ['item', 'uuid', 'quantity']
        extra_kwargs = {'quantity': {'required': True}}


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(), 
        queryset=User.objects.all(),
        slug_field='email'
    )
    order_items = OrderItemSerializer(many=True)
    order_status = OrderStatusField(source='*', required=False)
    payment_status = PaymentStatusField(source='*', required=False)
    payment_method = PaymentMethodField(source='*')

    class Meta:
        model = Order
        exclude = ['id', 'is_active', 'station']

    def validate(self, attrs):
        attrs = super().validate(attrs)
        order_items = attrs['order_items']
        out_of_stock_items = OrderItem.check_inventory(order_items)
        if out_of_stock_items:
            raise serializers.ValidationError(detail={
                'message': OUT_OF_STOCK_MESSAGE,
                'out_of_stock_items': [out_of_stock_items]
            })
        return attrs

    def _create_order_items(self, order_items_data, order):
        order_items = [OrderItem(**order_item_data, order=order) for order_item_data in order_items_data]
        order_items = OrderItem.objects.bulk_create(order_items)
        return order_items

    def _order_price_calculations(self, order, order_items):
        base_price = sum([order_item.item.price for order_item in order_items])
        order.base_price = base_price
        order.total_price = base_price
        order.order_status = OrderStatus.PROCESSING
        order.save()

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)
        order_items = self._create_order_items(order_items_data, order)
        self._order_price_calculations(order, order_items)
        OrderItem.deduct_inventory(order_items)
        return order

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
