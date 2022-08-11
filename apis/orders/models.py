import uuid
from django.contrib.auth import get_user_model
from django.db import models

from apis.orders.choices import (DISCOUNT_TYPE_CHOICES, ORDER_STATUS_CHOICES,
                                 PAYMENT_CHOICES, PAYMENT_STATUS_CHOICES)
from apis.orders.utils.order_generation import create_order_key
from apis.stations.models import Station, StationInventoryItem
from apis.base_models import BaseModel


User = get_user_model()


class Order(BaseModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    order_key = models.CharField(max_length=40, null=True, blank=True, unique=True, default=create_order_key)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_orders')
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='station_orders', null=True, blank=True)
    order_status = models.CharField(max_length=250, null=True, blank=True, choices=ORDER_STATUS_CHOICES)
    payment_status = models.CharField(max_length=250, null=True, blank=True, choices=PAYMENT_STATUS_CHOICES)
    base_price = models.FloatField(null=True, blank=True)
    total_price = models.FloatField(null=True, blank=True)
    service_charges = models.FloatField(null=True, blank=True)
    delivery_charges = models.FloatField(null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)
    discount_type = models.CharField(null=True, blank=True, choices=DISCOUNT_TYPE_CHOICES, max_length=30)
    tax = models.FloatField(null=True, blank=True)
    returned_amount = models.FloatField(null=True, blank=True)
    payment_method = models.CharField(max_length=250, null=True, blank=True, choices=PAYMENT_CHOICES)
    pickup_datetime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.order_key


class OrderItem(BaseModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    item = models.ForeignKey(StationInventoryItem, on_delete=models.CASCADE, related_name='order_item_item')
    quantity = models.IntegerField(default=1)
    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        return self.item.name
