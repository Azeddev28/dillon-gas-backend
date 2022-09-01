from django.db import models

from cities_light.models import City, Region

from apis.base_models import BaseModel


class DeliveryInfo(BaseModel):
    delivery_cost = models.FloatField()
    city = models.ForeignKey(City, related_name='city_delivery_info', on_delete=models.SET_NULL, null=True, blank=True)
    state = models.ForeignKey(Region, related_name='state_delivery_info', on_delete=models.SET_NULL, null=True, blank=True)
    min_delivery_time = models.CharField(max_length=30)
    max_delivery_time = models.CharField(max_length=30)
