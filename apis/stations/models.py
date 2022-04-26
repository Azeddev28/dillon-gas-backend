from django.db import models
from django.contrib.auth import get_user_model

from apis.base_models import BaseModel

User = get_user_model()


class Station(BaseModel):
    location = models.TextField()
    city = models.TextField()
    station_id = models.CharField(max_length=200)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='gas_station')

    class Meta:
        db_table = "stations"

    def __str__(self):
        return self.station_id


class StationInventory(BaseModel):
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='inventory')
    tax = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'inventory'
        verbose_name_plural = 'inventories'
