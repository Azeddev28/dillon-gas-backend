from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

from apis.base_models import BaseModel
from apis.ratings.utils.constants import MAXIMUM_STAR_RATING_VALUE, MINIMUM_STAR_RATING_VALUE
from apis.stations.models import StationInventoryItem

User = get_user_model()


class StarRating(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    star_count = models.FloatField(validators=[MinValueValidator(MINIMUM_STAR_RATING_VALUE), MaxValueValidator(MAXIMUM_STAR_RATING_VALUE)],)
    item = models.ForeignKey(StationInventoryItem, on_delete=models.CASCADE, related_name='ratings')
    
    def __str__(self):
        return f'{self.item.name} {self.star_count}'
