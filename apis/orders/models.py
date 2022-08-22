import uuid
from django.contrib.auth import get_user_model
from django.db import models

from apis.orders.choices import (DISCOUNT_TYPE_CHOICES, OrderStatus,
                                 PaymentMethods, PaymentStatus)
from apis.orders.utils.order_generation import create_order_key
from apis.stations.models import Station, StationInventoryItem
from apis.base_models import BaseModel


User = get_user_model()


class Order(BaseModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    order_number = models.CharField(max_length=40, null=True, blank=True, unique=True, default=create_order_key)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_orders')
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='station_orders', null=True, blank=True)
    order_status = models.IntegerField(null=True, blank=True, choices=OrderStatus.CHOICES, default=OrderStatus.PENDING)
    payment_status = models.IntegerField(null=True, blank=True, choices=PaymentStatus.CHOICES, default=PaymentStatus.PENDING)
    base_price = models.FloatField(null=True, blank=True)
    total_price = models.FloatField(null=True, blank=True)
    service_charges = models.FloatField(null=True, blank=True)
    delivery_charges = models.FloatField(null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)
    discount_type = models.CharField(null=True, blank=True, choices=DISCOUNT_TYPE_CHOICES, max_length=30)
    tax = models.FloatField(null=True, blank=True)
    payment_method = models.IntegerField(null=True, blank=True, choices=PaymentMethods.CHOICES, default=None)
    pickup_datetime = models.DateTimeField(null=True, blank=True)
    delivery_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.order_number


class OrderItem(BaseModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    item = models.ForeignKey(StationInventoryItem, on_delete=models.CASCADE, related_name='order_item_item')
    quantity = models.IntegerField(default=1)
    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        return self.item.name

    @classmethod
    def check_inventory(cls, raw_order_items):
        out_of_stock_items = [
            {
                'item': dict(inventory_item).get('item').uuid,
                'available_quantity': dict(inventory_item).get('item').quantity
            }
            for inventory_item in raw_order_items
            if dict(inventory_item).get('item').out_of_stock(dict(inventory_item).get('quantity'))
        ]
        return out_of_stock_items

    @classmethod
    def deduct_inventory(cls, order_items):
        station_inventory_items = [
            order_item.item for order_item in order_items
        ]
        updated_inventory = []
        for inventory_item, order_item in zip(station_inventory_items, order_items):
            inventory_item.quantity -= order_item.quantity
            updated_inventory.append(inventory_item)

        StationInventoryItem.objects.bulk_update(updated_inventory, ['quantity'])
