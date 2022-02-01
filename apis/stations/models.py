from django.db import models
from django.contrib.auth import get_user_model

from apis.base_models import TimeStamp

User = get_user_model()


class GasStation(TimeStamp):
    location = models.TextField()
    city = models.TextField()
    station_id = models.CharField(max_length=200)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='gas_station')

    def __str__(self):
        return self.station_id

class Inventory(TimeStamp):
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    station = models.ForeignKey(
        GasStation, on_delete=models.CASCADE, related_name='inventory')
