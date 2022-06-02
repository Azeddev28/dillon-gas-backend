import uuid
from django.db import models

from apis.base_models import BaseModel
from apis.inventory.utils.media_paths import category_image_path, item_image_path
from apis.promotions.models import Promotion
from apis.stations.models import Station


class Category(BaseModel):
    name = models.CharField(max_length=200, unique=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    image = models.ImageField(upload_to=category_image_path, null=True, blank=True)
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="station_categories", null=True, blank=True)
    promotion = models.ForeignKey(Promotion, related_name="category_promotions", on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.name


class Item(BaseModel):
    name = models.CharField(max_length=200)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    image = models.ImageField(upload_to=item_image_path, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_items")
    description = models.TextField(null=True, blank=True)
    bar_code = models.CharField(max_length=20, unique=True)
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="station_items", null=True, blank=True)
    weight = models.CharField(default=None, null=True, blank=True, max_length=30)

    def __str__(self):
        return self.name
