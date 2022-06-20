import uuid
from django.contrib.auth import get_user_model
from django.db import models

from apis.base_models import BaseModel

User = get_user_model()


class Wallet(BaseModel):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wallet')


# class PaymentCard(BaseModel):
#     card_number = models.CharField(max_length=200)
#     cvv =  models.CharField(max_length=3)
#     expiry_month = models.CharField(max_length=2)
#     expiry_year = models.CharField(max_length=2)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payment_cards')
