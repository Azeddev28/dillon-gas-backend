from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from apis.users.models import DeliveryAgent
from apis.users.utils.choices import ROLES

from apis.wallets.models import Wallet

User = get_user_model()


# @receiver(post_save, sender=User)
# def create_wallet_on_registration(sender, instance, created, **kwargs):
#     if created and not instance.is_superuser:
#         Wallet.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_delivery_agent(sender, instance, created, **kwargs):
    if created and instance.role == ROLES[0][0]:
        DeliveryAgent.objects.create(user=instance)
