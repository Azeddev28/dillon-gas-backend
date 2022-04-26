
import uuid
from django.db import models

from apis.base_models import BaseModel
from apis.promotions.utils.media_paths import promotion_image_path
from apis.stations.models import Station


class Promotion(BaseModel):
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="station_promotions", null=True, blank=True, default=None)
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=500, blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to=promotion_image_path, null=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.title
