from django.db import models
from django.contrib.auth import get_user_model

from apis.base_models import TimeStamp

User = get_user_model()


class Delivery(TimeStamp):
    delivery_agent = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='agent_deliveries')
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='customer_deliveries')
    address = models.TextField()
    order_placed = models.DateTimeField()
    delivered_at = models.DateTimeField()
    status = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'deliveries'