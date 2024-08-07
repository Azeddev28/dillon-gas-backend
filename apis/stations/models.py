from django.db import models
from django.contrib.auth import get_user_model
import uuid

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


class StationInventoryItem(BaseModel):
    item = models.ForeignKey('inventory.Item', on_delete=models.CASCADE, related_name='inventory')
    quantity = models.IntegerField()
    price = models.FloatField()
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='inventory', null=True, blank=True)
    tax = models.FloatField(null=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        db_table = 'inventory'
        verbose_name_plural = 'inventories'

    @property
    def name(self):
        return self.item.name

    def out_of_stock(self, quantity):
        if self.quantity < quantity:
            return True

        return False

    def __str__(self):
        return self.name
