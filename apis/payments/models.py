from django.db import models
from django.contrib.auth import get_user_model

from apis.base_models import TimeStamp

User = get_user_model()


class Wallet(TimeStamp):
    wallet_id = models.CharField(max_length=200)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_wallet')
    amount = models.FloatField()