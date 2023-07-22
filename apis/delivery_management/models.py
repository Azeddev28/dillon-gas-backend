from django.db import models
from django.contrib.auth import get_user_model

from cities_light.models import City, Region

from apis.base_models import BaseModel
from apis.base_models import BaseModel
from apis.orders.models import Order

User = get_user_model()


class DeliveryInfo(BaseModel):
    delivery_cost = models.FloatField()
    city = models.ForeignKey(City, related_name='city_delivery_info', on_delete=models.SET_NULL, null=True, blank=True)
    state = models.ForeignKey(Region, related_name='state_delivery_info', on_delete=models.SET_NULL, null=True, blank=True)
    min_delivery_time = models.CharField(max_length=30)
    max_delivery_time = models.CharField(max_length=30)


City.add_to_class(
    'delivery_enabled',
    models.BooleanField(default=False),
)

Region.add_to_class(
    'delivery_enabled',
    models.BooleanField(default=False),
)


class OrderDelivery(BaseModel):
    delivery_agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='agent_orders')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_delivery')
    pickup_datetime = models.DateTimeField(null=True, blank=True)
    delivery_datetime = models.DateTimeField(null=True, blank=True)
    order_active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Order Deliveries'
        unique_together = ('delivery_agent', 'order')