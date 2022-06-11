import uuid
from django.db import models
from django.contrib.auth import get_user_model

from apis.base_models import TimeStamp
from apis.transactions.choices import TransactionStatusChoices, WalletTransactionTypeChoices

User = get_user_model()


class Transaction(TimeStamp):
    status = models.IntegerField(choices=TransactionStatusChoices.CHOICES, default=TransactionStatusChoices.PENDING)
    user = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)
    amount = models.FloatField()
    reference = models.UUIDField(default=uuid.uuid4, unique=True)


class WalletTransaction(Transaction):
    transaction_type = models.IntegerField(choices=WalletTransactionTypeChoices.CHOICES)
