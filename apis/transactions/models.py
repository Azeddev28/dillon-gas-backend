from django.db import models
from django.contrib.auth import get_user_model

from apis.base_models import TimeStamp

User = get_user_model()


class Transaction(TimeStamp):
    status = models.CharField(max_length=100)
    user = models.ForeignKey(
        User, related_name='transactions', on_delete=models.CASCADE)
    product = models.CharField(max_length=200)
    amount = models.FloatField()
