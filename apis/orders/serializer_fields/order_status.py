from rest_framework import serializers

from apis.orders.choices import OrderStatus


class OrderStatusField(serializers.Field):

    def to_representation(self, value):
        return value.get_order_status_display()

    def to_internal_value(self, data):
        order_status_value = getattr(OrderStatus, data)
        return {'order_status': order_status_value}
