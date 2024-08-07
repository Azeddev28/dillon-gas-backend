from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from apis.wallets.models import Wallet

User = get_user_model()


# @receiver(post_save, sender=User)
# def create_wallet_on_registration(sender, instance, created, **kwargs):
#     if created and not instance.is_superuser:
#         Wallet.objects.create(user=instance)
