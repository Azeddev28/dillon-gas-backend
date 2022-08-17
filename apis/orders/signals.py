from django.dispatch import receiver
from django.db.models.signals import post_save

from apis.orders.models import Order
from ..services.email_service import EmailService


@receiver(post_save, sender=Order)
def notify_delivery_agents(sender, created, instance, **kwargs):
    if created:
        pass


@receiver(post_save, sender=Order)
def order_tracking(sender, created, instance, **kwargs):
    if created:
        email_service = EmailService(
            'Order Tracking',
            [instance.customer.email, ],
            'email_templates/order_tracking.html',
            {}
        )
        email_service.start()
